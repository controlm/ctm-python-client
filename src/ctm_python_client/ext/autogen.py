import jinja2
import urllib3
import typing
import requests
import attrs

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__all__ = ['generate_ai_plugins_classes']

IF_PLUGINS = ['ABR092025', 'ZWB072025', 'ASM0220223', 'ZLA112022', 'ABK042023', 'ZBA042022', 'ODS052024', 'ALM012024', 'JEN022024', 'AAP092024', 'ADM062025', 'ADB112022', 'ANS032024', 'AAR072022', 'GDM082023', 'TAB072023', 'ADY122023', 'DTG022025', 'TER102023', 'PBI082024', 'COM032023', 'GDF032022', 'PDY092024', 'ADS102024', 'RST062023', 'ABA092022', 'BAK092023', 'ABB092025', 'NBU032025', 'MBI042022', 'ZML022023', 'ADF062021', 'MFB062025', 'ABY122023', 'ACF082023', 'SBT032025', 'BOO032022', 'DTG052025', 'RMQ082024', 'VMW102024', 'AEC082022', 'MFL022023', 'AAT052023', 'GDQ112023', 'ODI032024', 'TDM052022', 'ARS112024', 'DBX032022', 'AST072024', 'MFW022023', 'AMM082023', 'AWX122024', 'CMR022024', 'GLU062021', 'SNF092022', 'AAF112024', 'VNB032025', 'ZRM082023', 'FVT032025', 'ATR122022', 'BEC032025', 'GEA072025', 'AHD062022', 'VBR062025', 'GVM062022', 'ADP122022', 'GDU102023', 'ASQ032024', 'ODF0420241', 'GCC052024', 'GWF092023', 'AQS012023', 'CCI012025', 'UIP072021', 'GBQ102022', 'GDP042022', 'AMW112024', 'APP022025', 'SFI122022', 'DSW122024', 'NFI042024', 'GDR052023', 'ADO112023', 'AEM072022', 'TDO042024', 'GCR042024', 'ZFN032022', 'SOP072023', 'GBA032023', 'GVA092025', 'QLC092022', 'ZSY062022', 'ICS032022', 'DBT042023', 'GIT092025', 'MAT022025', 'ZDX112021', 'ZVM062022', 'ACS042023', 'DSL122024', 'ASB012025', 'KBN062023', 'GFU012023', 'OVM012024', 'RBK072025', 'ASF012023']


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
