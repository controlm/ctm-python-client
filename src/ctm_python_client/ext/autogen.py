import jinja2
import urllib3
import typing
import requests
import attrs

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__all__ = ['generate_ai_plugins_classes']

IF_PLUGINS = ['ASB012025', 'GDR052023', 'AMM082023', 'ABY122023', 'JEN022024', 'ADS102024', 'MFW022023', 'JCP102025', 'GCR042024', 'ASQ032024', 'GDQ112023', 'FVT032025', 'ZML022023', 'MFL022023', 'GEA072025', 'BEC032025', 'ABK042023', 'OFC042026', 'ZVM062022', 'ADO112023', 'AHD062022', 'ZSY062022', 'SBT032025', 'ZDX112021', 'ODF062024', 'DBX032022', 'AWX122024', 'MPA032026', 'DBT042023', 'ADM062025', 'TAB072023', 'DSL122024', 'BOO032022', 'KBN062023', 'APK032026', 'DTG052025', 'MAT022025', 'ABB092025', 'ODF0420241', 'SIB062025', 'ADY122023', 'ICS032022', 'SNC022026', 'LAN012026', 'QLC092022', 'SNF092022', 'PDY092024', 'DTG022025', 'ABR092025', 'GVM062022', 'GDF032022', 'VNB032025', 'ZBA042022', 'COM032023', 'SDS122025', 'ZFN032022', 'NFI042024', 'ASM0220223', 'TDM052022', 'OVM012024', 'RST062023', 'GIT092025', 'OFC032026', 'AEC082022', 'TER102023', 'CCI012025', 'ATR122022', 'VBR062025', 'ANS032024', 'ASF012023', 'ABA092022', 'RMQ082024', 'ODS052024', 'BAK092023', 'ZWB072025', 'ACS042023', 'ZLA112022', 'RBK072025', 'ACF082023', 'GVA092025', 'MBI042022', 'ODI032024', 'ADB112022', 'GLU062021', 'AST072024', 'SOP072023', 'NBU032025', 'GCC052024', 'ALM012024', 'CMR022024', 'GDU102023', 'ZRM082023', 'TDO042024', 'ADF062021', 'AMW112024', 'AQS012023', 'VMW102024', 'ADP122022', 'APP022025', 'AEM072022', 'AAP092024', 'GBA032023', 'UIP072021', 'CRW122025', 'MFB062025', 'GWF092023', 'ARS112024', 'GDP042022', 'AAR072022', 'AAT052023', 'GBQ102022', 'SFI122022', 'PBI082024', 'GFU012023', 'AAF112024', 'GDM082023', 'DSW122024']


imports_str = '''from aapi import *
import attrs

'''
template_job = jinja2.Template('''
@attrs.define
class {{plugin.class_name}}(AIJob):
    _type = AIJob.type_field('{{plugin.type_field}}')

    {% for p in plugin.mandatory_properties %}
    {{p[0]}} = AIJob.field('{{p[1]}}')
    {%endfor%}

    {% for p in plugin.optional_properties %}
    {{p[0]}} = AIJob.field_optional('{{p[1]}}', default='{{p[2]}}')
    {%endfor%}    
    ''')

template_cp = jinja2.Template('''
@attrs.define
class {{plugin.class_name}}(AIConnectionProfile):
    _type = AIConnectionProfile.type_field('{{plugin.type_field}}')

    {% for p in plugin.mandatory_properties %}
    {{p[0]}} = AIConnectionProfile.field('{{p[1]}}')
    {%endfor%}

    {% for p in plugin.optional_properties %}
    {{p[0]}} = AIConnectionProfile.field_optional('{{p[1]}}', default='{{p[2]}}')
    {%endfor%}    
    ''')


@attrs.define
class Plugin:
    job_name: str
    cp_name: str
    job_definition: typing.Dict[str, str]
    cp_definition: typing.Dict[str, str]

    plugin_type: str


@attrs.define
class AIPluginCustomDefinition:
    class_name: str
    type_field: str

    mandatory_properties: typing.List[typing.Tuple[str]]
    optional_properties: typing.List[typing.Tuple[str]]
    comments: typing.List[str]


def create_ai_custom_definitions(ai_plugin: Plugin) -> typing.Tuple[AIPluginCustomDefinition, AIPluginCustomDefinition]:
    plugin_name = ai_plugin.job_name.split(':')[-1]
    plugin_cp_name = ai_plugin.cp_name.split(':')[-1]
    job = {
        'class_name': 'AIJob'+plugin_name.capitalize().replace(" ", ""),
        'type_field': plugin_name,
        'mandatory_properties': [],
        'optional_properties': [],

        'comments': [f'Auto generated class for {plugin_name}']
    }
    cp = {
        'class_name': 'ConnectionProfileAI'+plugin_cp_name.capitalize().replace(" ", ""),
        'type_field': plugin_cp_name,
        'mandatory_properties': [],
        'optional_properties': [],
        'comments': [f'Auto generated class for {plugin_cp_name}']
    }

    for k, v in ai_plugin.job_definition.items():
        if not k.startswith('AI-'):
            continue

        if k == 'AI-Connection Profile':
            continue

        domain_name = v.get('DomainName')
        if domain_name in ai_plugin.job_definition['Defaults']:
            default = ai_plugin.job_definition['Defaults'][domain_name]

            job['optional_properties'].append((
                domain_name.split(r'%%UCM-')[1].lower(),
                k.split('AI-')[1],
                default
            ))
        else:
            job['mandatory_properties'].append((
                domain_name.split(r'%%UCM-')[1].lower(),
                k.split('AI-')[1],
                None
            ))

    for k, v in ai_plugin.cp_definition.items():
        if not k.startswith('AI-'):
            continue

        if k in ['AI-Run As', 'AI-RunAs-Pass']:
            continue

        domain_name = v.get('DomainName')
        if domain_name in ai_plugin.cp_definition['Defaults']:
            default = ai_plugin.cp_definition['Defaults'][domain_name]

            cp['optional_properties'].append((
                domain_name.lower(),
                k.split('AI-')[1],
                default
            ))
        else:
            cp['mandatory_properties'].append((
                domain_name.lower(),
                k.split('AI-')[1],
                None
            ))

    return (AIPluginCustomDefinition(**job), AIPluginCustomDefinition(**cp))


def get_all_plugins_versions_from_url(url: str) -> typing.Dict[str, str]:
    r = requests.get(url=url, verify=False)

    return r.json()


def parse_plugin(url):
    r = requests.get(url, verify=False)
    plugin = {}

    for k, v in r.json().items():
        if k.startswith('Job:'):
            plugin["job_name"] = k
            plugin["job_definition"] = v
            continue

        if k.startswith('ConnectionProfile:'):
            plugin["cp_name"] = k
            plugin["cp_definition"] = v
            continue

    if 'Aliases' in r.json():
        plugin['plugin_type'] = 'AI'
    else:
        plugin['plugin_type'] = 'IF'

    return Plugin(**plugin)
    # return plugin


def get_all_plugins(host: str, port: str = '8443', exlude_list=[]):
    versions = get_all_plugins_versions_from_url(
        f'https://{host}:{port}/automation-api/ai-repo/deployed_plugins.json')

    res = []
    for plugin, version in versions.items():
        if plugin in exlude_list:
            continue

        url = f'https://{host}:{port}/automation-api/ai-repo/{plugin}/v{version}/descriptorDictionary{plugin}.json'

        res.append(parse_plugin(url))

    return res


def create_class_code(plugin_definitions):
    job_str = template_job.render(plugin=plugin_definitions[0])
    cp_str = template_cp.render(plugin=plugin_definitions[1])

    return (job_str, cp_str)


def generate_ai_plugins_classes(host: str = 'localhost', port: str = '8443', output_file: str = 'generated.py'):
    plugins = get_all_plugins(host=host, port=port, exlude_list=IF_PLUGINS)
    definitions = [create_ai_custom_definitions(plugin) for plugin in plugins]
    with open(output_file, 'w') as f:
        f.write(imports_str)

        for definition in definitions:
            def_str = create_class_code(definition)
            f.write(f'''

# Auto generated code for AI Plugin {definition[0].type_field}
            ''')
            f.write(def_str[0])  # JOB
            f.write(def_str[1])  # Connection Profile
