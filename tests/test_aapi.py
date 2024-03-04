
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
    workflow.add(aapi.JobCommand('TestJob', command='ls -lt', run_as='workbench'), inpath='TestFolder')

    newworkflow = BaseWorkflow()
    newworkflow.copy_from(workflow=workflow)

    assert newworkflow.get("TestFolder").dumps_aapi(indent=2) == workflow.get("TestFolder").dumps_aapi(indent=2)

    o = json.loads('{\n  "Type": "Folder",\n  "TestJob": {\n    "Type": "Job:Command",\n    "RunAs": "workbench",\n    "Command": "ls -lt"\n  },\n  "RunAs": "workbench"\n}')
    assert newworkflow.get("TestFolder").as_aapi_dict() == o

def test_connecting_jobs():
    workflow = Workflow(Environment.create_workbench("refael"), WorkflowDefaults(run_as='workbench'), skip_initial_authentication=True)
    firstjob = workflow.add(
        aapi.JobCommand('JobToConnect1', command="first"),
        inpath='TestFolder'
    )

    secondjob = workflow.add(
        aapi.JobCommand('JobToConnect2', command="second"),
        inpath='TestFolder'
    )
    workflow.connect(firstjob, secondjob)

def test_chaining_jobs():
    workflow = Workflow(Environment.create_workbench("refael"), WorkflowDefaults(run_as='workbench'), skip_initial_authentication=True)
    workflow.chain(
        [
            aapi.JobCommand('FirstTestJob', "First"),
            aapi.JobCommand('SecondTestJob', "Second"),
            aapi.JobCommand('ThirdTestJob', "Third", run_as_dummy=True),
        ],
        inpath='ChainedJobs'
    )

def test_events():
    job = aapi.JobCommand('Job1', command='echo Hello')
    
    waitForEventList = aapi.WaitForEvents([aapi.Event(event="wait1"), aapi.Event(event="wait2", date=aapi.Event.Date.AnyDate)])
    job.event_list.append(waitForEventList)

    deleteEventListObject = aapi.DeleteEvents([aapi.EventOutDelete(event="delete")])
    job.event_list.append(deleteEventListObject)

    addEventListObject1 = aapi.AddEvents([aapi.EventOutAdd(event="add1")])
    job.event_list.append(addEventListObject1)
    
    addEventListObject2 = aapi.AddEvents([aapi.EventOutAdd(event="add2",date=aapi.Event.Date.NoDate)])
    job.add_events_list.append(addEventListObject2)
    
    assert any(isinstance(obj, aapi.WaitForEvents) and any(event.event == 'wait2' for event in obj.events) for obj in job.event_list)
    assert any(isinstance(obj, aapi.DeleteEvents) and any(event.event == 'delete' for event in obj.events) for obj in job.event_list)
    assert any(isinstance(obj, aapi.AddEvents) and any(event.event == 'add1' for event in obj.events) for obj in job.event_list)
    assert any(isinstance(obj, aapi.AddEvents) and any(event.event == 'add2' for event in obj.events) for obj in job.add_events_list)
    
    assert json.loads(job.dumps_aapi())
