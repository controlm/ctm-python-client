import jinja2
import urllib3
import typing
import requests
import attrs

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

__all__ = ['generate_ai_plugins_classes']

IF_PLUGINS = ['ZFN032022', 'ANS032024', 'OVM012024', 'ASM0220223', 'TAB072023', 'ADY122023', 'ABY122023', 'ODF0420241', 'NFI042024', 'AQS012023', 'SFI122022', 'KBN062023', 'ADO112023', 'ABA092022', 'AMM082023', 'GCC052024', 'AEC082022', 'ASF012023', 'TDM052022', 'BOO032022', 'ICS032022', 'GBQ102022', 'ZSY062022', 'MFW022023', 'GFU012023', 'AAR072022', 'RST062023', 'ALM012024', 'ASQ032024', 'TER102023', 'ZBA042022', 'ZRM082023', 'AHD062022', 'GVM062022', 'CMR022024', 'COM032023', 'GBA032023', 'DBX032022', 'SOP072023', 'SNF092022', 'ADB112022', 'ACF082023', 'ZVM062022', 'GDM082023', 'TDO042024', 'GDU102023', 'JEN022024', 'GLU062021', 'AAT052023', 'UIP072021', 'ATR122022', 'ZML022023', 'ZLA112022', 'GDR052023', 'QLC092022', 'BAK092023', 'ACS042023', 'ABK042023', 'ODI032024', 'MBI042022', 'ADF062021', 'DBT042023', 'ODS052024', 'ADP122022', 'MFL022023', 'ZDX112021', 'GDP042022', 'GDQ112023', 'GWF092023', 'AEM072022', 'GDF032022']


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
