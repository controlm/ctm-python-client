import enum
import json
import random
import typing

import attrs

from ctm_python_client.core.comm import Environment
from ctm_python_client.core.monitoring import RunMonitor


class AAPIJob:
    pass


class AAPIObject:
    def as_aapi_dict(self, ignore_event_type=True):
        
        # Import inside the method to prevent circular import issues
        from aapi.ifbase import IfCompletionStatus  
        
        res = {}

        if '_type' in attrs.fields_dict(self.__class__):
            is_condition_or_event = self._type.startswith(('Condition', 'Event'))
    
            if ignore_event_type:
                if not is_condition_or_event:
                    res['Type'] = self._type
            elif self._type.startswith('Event'):
                res['Type'] = self._type

                
        if attrs.has(self):
            for field in attrs.fields(self.__class__):
                value = self.__getattribute__(field.name)
                aapi_repr = field.metadata.get("_aapi_repr_")

                if value in [None, [], {}]:
                    continue

                if aapi_repr:
                    if "_type_aapi_" in field.metadata:
                        if "_hide_type_" in field.metadata:
                            if "Type" in res:
                                res.__delitem__("Type")
                        continue
                    if "as_aapi_dict" in dir(value):
                        res[aapi_repr] = value.as_aapi_dict()
                    elif isinstance(value, list):
                        res[aapi_repr] = [
                            (o.as_aapi_dict() if "as_aapi_dict" in dir(o) else o)
                            for o in value
                        ]
                    elif isinstance(value, enum.Enum):
                        res[aapi_repr] = value.value
                    else:
                        res[aapi_repr] = value

                elif field.metadata.get("_abstract_aapi_container_"):
                    for obj in value:
                        obj_ignore_type = ignore_event_type
                        if isinstance(self, IfCompletionStatus):
                            obj_ignore_type = False  
                        res[obj.object_name] = obj.as_aapi_dict(ignore_event_type=obj_ignore_type)

        else:
            res["attrsibutes_valid"] = False

        return res

    def dumps_aapi(self, indent=None):
        return json.dumps(self.as_aapi_dict(), indent=indent)

    def dump_aapi(self, f, indent=None):
        return json.dump(self.as_aapi_dict(), f, indent=indent)

    def as_dict(self):
        return attrs.asdict(self)

    def run_on_demand(
        self,
        environment: Environment,
        skip_initial_authentication: bool = False,
        inpath: str = f"run_on_demand{random.randint(100,999)}",
        controlm_server: str = None,
        run_as: str = None,
        host: str = None,
        application: str = None,
        sub_application: str = None,
        skip_login: bool = False,
        file_path: str = None,
        delete_afterwards: bool = True,
        open_in_browser: str = None,
    ) -> RunMonitor:
        # Import circular dependency
        from aapi import Folder
        from ctm_python_client.core.workflow import Workflow, WorkflowDefaults

        if (hasattr(self, "_type") and "Job" in self._type) or (
            hasattr(self, "job_list")
            and self.job_list is not None
            and len(self.job_list) > 0
        ):
            try:
                on_demand_workflow = Workflow(
                    environment,
                    WorkflowDefaults(
                        controlm_server=controlm_server,
                        run_as=run_as,
                        host=host,
                        application=application,
                        sub_application=sub_application,
                    ),
                    skip_initial_authentication=skip_initial_authentication,
                )
                if isinstance(self, Folder):
                    on_demand_workflow.add(self)
                else:
                    on_demand_workflow.add(self, inpath=inpath)

                return on_demand_workflow.run_on_demand(
                    skip_login=skip_login,
                    file_path=file_path,
                    delete_afterwards=delete_afterwards,
                    open_in_browser=open_in_browser,
                )
            except Exception as e:
                if hasattr(e, "body"):
                    errors = [
                        err.get("message", "") + " " + err.get("item", "")
                        for err in json.loads(e.body)["errors"]
                    ]
                    raise RuntimeError(f"AAPI request failed: {', '.join(errors)}")
                else:
                    raise e
            finally:
                on_demand_workflow.clear_all()
        else:
            raise Exception("Run is not allowed for json without jobs")
