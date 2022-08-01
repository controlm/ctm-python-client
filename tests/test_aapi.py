
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


def test_parser():
    # test that the parser can load
    from aapi.parser import AAPIParser

def test_parse_object():
    jsondata = json.loads('''
    {
    "Folder_Test" : {
        "Type" : "Folder",
        "ControlmServer" : "LocalControlM",
        "ActiveRetentionPolicy" : "CleanEndedOK",
        "RunAs" : "controlm",
        "CreatedBy" : "emuser1",
        "When" : {
        "RuleBasedCalendars" : {
            "Included" : [ "EVERYDAY" ],
            "EVERYDAY" : {
            "Type" : "Calendar:RuleBased",
            "When" : {
                "DaysRelation" : "OR",
                "WeekDays" : [ "NONE" ],
                "MonthDays" : [ "ALL" ]
            }
            }
        }
        },
        "Workflow" : {
        "Type" : "SubFolder",
        "AdjustEvents" : false,
        "CreatedBy" : "emuser1",
        "When" : {
            "DaysRelation" : "OR",
            "RuleBasedCalendars" : {
            "Included" : [ "USE PARENT" ]
            }
        },
        "FirstJob" : {
            "Type" : "Job:Command",
            "CreatedBy" : "emuser1",
            "RunAs" : "controlm",
            "Command" : "ls -l",
            "When" : {
            "WeekDays" : [ "NONE" ],
            "MonthDays" : [ "ALL" ],
            "DaysRelation" : "OR"
            },
            "Output" : { },
            "eventsToWaitFor" : {
            "Type" : "WaitForEvents",
            "Events" : [ {
                "Event" : "StarterJob-TO-FirstJob"
            } ]
            },
            "eventsToDelete" : {
            "Type" : "DeleteEvents",
            "Events" : [ {
                "Event" : "StarterJob-TO-FirstJob"
            } ]
            }
        },
        "eventsToAdd" : {
            "Type" : "AddEvents",
            "Events" : [ {
            "Event" : "Workflow-TO-ServiceJob"
            } ]
        }
        },
        "ServiceJob" : {
        "Type" : "Job:SLAManagement",
        "ServiceName" : "test_server",
        "ServicePriority" : "3",
        "JobRunsDeviationsTolerance" : "3",
        "CreatedBy" : "emuser1",
        "RunAs" : "controlm",
        "CompleteBy" : {
            "Time" : "12:00",
            "Days" : "0"
        },
        "When" : {
            "WeekDays" : [ "NONE" ],
            "MonthDays" : [ "ALL" ],
            "DaysRelation" : "OR"
        },
        "Output" : { },
        "eventsToWaitFor" : {
            "Type" : "WaitForEvents",
            "Events" : [ {
            "Event" : "Workflow-TO-ServiceJob"
            } ]
        },
        "eventsToDelete" : {
            "Type" : "DeleteEvents",
            "Events" : [ {
            "Event" : "Workflow-TO-ServiceJob"
            } ]
        }
        },
        "StarterJob" : {
        "Type" : "Job:Dummy",
        "Confirm" : true,
        "CreatedBy" : "emuser1",
        "RunAs" : "DUMMYUSR",
        "When" : {
            "WeekDays" : [ "NONE" ],
            "MonthDays" : [ "ALL" ],
            "DaysRelation" : "OR"
        },
        "Output" : { },
        "eventsToAdd" : {
            "Type" : "AddEvents",
            "Events" : [ {
            "Event" : "StarterJob-TO-FirstJob"
            } ]
        }
        }
    }
    }
    ''')

    from aapi.parser import AAPIParser

    folder: aapi.Folder = AAPIParser.parse_typed_object('Folder_Test', jsondata['Folder_Test'])

    # assert that the dictionary from folder is identical to the json data
    assert folder.as_aapi_dict() == jsondata['Folder_Test']

    assert folder.object_name == 'Folder_Test'