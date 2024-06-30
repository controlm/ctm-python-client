
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

def test_job_in_folder_run_as():
    workflow = Workflow(Environment.create_workbench("refael"), WorkflowDefaults(run_as='workbench'), skip_initial_authentication=True)
    job_command = aapi.JobCommand('TestJob', command='echo Hello')
    
    sla_job = aapi.JobSLAManagement('ForecastSLA',
                       service_name='ForecastSLA',
                       service_priority='1',
                       job_runs_deviations_tolerance='1',
                       complete_in=aapi.JobSLAManagement.CompleteIn(time='00:15'),
                       complete_by=aapi.JobSLAManagement.CompleteBy(
                           time='21:40', days='3'),
                       average_run_time_tolerance=aapi.JobSLAManagement.AverageRunTimeTolerance(
                           average_run_time='15',
                           units=aapi.JobSLAManagement.AverageRunTimeTolerance.Units.Minutes
                       ))
    
    subfolder = aapi.SubFolder('SubFolder')
    folder = aapi.Folder("TestFolder",
                         sub_folder_list=[subfolder],
                         job_list=[sla_job, job_command]
                         )
    workflow.add(folder)
    # {"TestFolder": {"Type": "Folder", "ForecastSLA": {"Type": "Job:SLAManagement", "RunAs": "workbench", "ServiceName": "ForecastSLA", "ServicePriority": "1", "JobRunsDeviationsTolerance": "1", "AverageRunTimeTolerance": {"AverageRunTime": "15", "Units": "Minutes"}, "CompleteBy": {"Time": "21:40", "Days": "3"}, "CompleteIn": {"Time": "00:15"}}, "TestJob": {"Type": "Job:Command", "RunAs": "workbench", "Command": "echo Hello"}, "RunAs": "workbench", "SubFolder": {"Type": "SubFolder", "RunAs": "workbench"}}}
    o = json.loads('''
        {
        "Type": "Folder",
        "ForecastSLA": {
            "Type": "Job:SLAManagement",
            "RunAs": "workbench",
            "ServiceName": "ForecastSLA",
            "ServicePriority": "1",
            "JobRunsDeviationsTolerance": "1",
            "AverageRunTimeTolerance": {
                "AverageRunTime": "15", 
                "Units": "Minutes"
            },
            "CompleteBy": {
                "Time": "21:40", 
                "Days": "3"
            },
            "CompleteIn": {
                "Time": "00:15"
                }
            },
            "TestJob": {
                "Type": "Job:Command",
                "RunAs": "workbench",
                "Command": "echo Hello"
            },
            "RunAs": "workbench",
            "SubFolder": {
                "Type": "SubFolder", 
                "RunAs": "workbench"
            }
        }
                   ''')
    assert workflow.get("TestFolder").as_aapi_dict() == o
    
