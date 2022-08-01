
import json
import aapi

def test_json_generation():
    folder = aapi.Folder('MyFolder', run_as='controlm')
    folder.job_list.append(aapi.JobCommand('JC1', command='ls -l'))
    folder.job_list.append(aapi.JobAWSLambda('JAL1', connection_profile='CPAWS', function_name='fname'))    

    o = json.loads(folder.dumps_aapi(indent=2))        
    assert o == folder.as_aapi_dict()


    o = json.loads('''
    {
        "Type": "Folder",
        "JC1": {
            "Type": "Job:Command",
            "Command": "ls -l"
        },
        "JAL1": {
            "Type": "Job:AWS:Lambda",
            "ConnectionProfile": "CPAWS",
            "FunctionName": "fname"
        },
        "RunAs": "controlm"

    }
    ''')

    assert o == folder.as_aapi_dict()
