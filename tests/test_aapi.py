
import json
import aapi
from ctm_python_client.core.workflow import Workflow, WorkflowDefaults, BaseWorkflow
from ctm_python_client.core.comm import Environment


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

def test_copy_workflow():
    workflow = Workflow(Environment.create_workbench("refael"), WorkflowDefaults(run_as='workbench'), skip_initial_authentication=True)
    workflow.add(aapi.JobCommand('MyFirstJob', command='ls -lt', run_as='workbench'), inpath='MyFirstFolder')

    newworkflow = BaseWorkflow()
    newworkflow.copy_from(workflow=workflow)

    assert newworkflow.get("MyFirstFolder").dumps_aapi(indent=2) == workflow.get("MyFirstFolder").dumps_aapi(indent=2)

    o = json.loads('{\n  "Type": "Folder",\n  "MyFirstJob": {\n    "Type": "Job:Command",\n    "RunAs": "workbench",\n    "Command": "ls -lt"\n  },\n  "RunAs": "workbench"\n}')
    assert newworkflow.get("MyFirstFolder").as_aapi_dict() == o
