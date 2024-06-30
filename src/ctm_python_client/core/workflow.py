import abc
import typing
import attrs
import json
import pathlib
import random
import tempfile
import collections
import copy

from aapi import *
from ctm_python_client.core.comm import AAPIClientResponse, AbstractAAPIClient, Environment, EnvironmentMode, OnPremAAPIClient, SaasAAPIClient, sanitize_output
from ctm_python_client.core.monitoring import RunMonitor

__all__ = ['AbstractWorkflow', 'WorkflowDefaults', 'BaseWorkflow', 'Workflow']


class AbstractWorkflow(abc.ABC):
    @abc.abstractclassmethod
    def add(self, ):
        pass

    @abc.abstractclassmethod
    def chain(self, ):
        pass

    @abc.abstractclassmethod
    def connect(self,):
        pass

    @abc.abstractclassmethod
    def get(self,):
        pass

    @abc.abstractclassmethod
    def get_objects(self,):
        pass

    @abc.abstractclassmethod
    def dump_json(self,):
        pass

    @abc.abstractclassmethod
    def dumps_json(self,):
        pass


# class AbstractWorkflowManager(AbstractWorkflow):

#     @abc.abstractclassmethod
#     def build(self, ):
#         pass

#     @abc.abstractclassmethod
#     def deploy(self,):
#         pass

#     @abc.abstractclassmethod
#     def run(self,):
#         pass


@attrs.define(kw_only=True)
class WorkflowDefaults:
    controlm_server: str = attrs.field(
        default=None, metadata={'applyon': ['Folder', 'SimpleFolder']})
    run_as: str = attrs.field(default=None, metadata={'applyon': [
                              'Folder', 'SimpleFolder', 'SubFolder', 'Job']})
    host: str = attrs.field(default=None, metadata={'applyon': ['Job']})
    when: Job.When = attrs.field(default=None, metadata={
                                 'applyon': ['Folder', 'Job']})
    application: str = attrs.field(default=None, metadata={'applyon': [
                                   'Folder', 'SimpleFolder', 'SubFolder', 'Job']})
    sub_application: str = attrs.field(default=None, metadata={'applyon': [
                                       'Folder', 'SimpleFolder', 'SubFolder', 'Job']})


class BaseWorkflow(AbstractWorkflow):
    def __init__(self, defaults: WorkflowDefaults = None) -> None:
        super().__init__()

        self._definitions = {}
        self._connections = {}

        self.defaults = defaults if defaults else WorkflowDefaults()

    def clear_all(self):
        self._definitions = {}
        self._connections = {}

    def _apply_defaults_for_type(self, obj: typing.Any, type_: str):
        if not obj:
            return
        else:
            for field in attrs.fields(WorkflowDefaults):
                if type_ in field.metadata.get('applyon') \
                        and self.defaults.__getattribute__(field.name):
                    if obj.__getattribute__(field.name) is None:
                        obj.__setattr__(
                            field.name, self.defaults.__getattribute__(field.name))

    def _apply_defaults_for_job(self, obj: Job):
        self._apply_defaults_for_type(obj, 'Job')

    def _apply_defaults_for_folder(self, obj: Folder):
        self._apply_defaults_for_type(obj, 'Folder')
        list(map(self._apply_defaults_for_SubFolder, obj.sub_folder_list))
        list(map(self._apply_defaults_for_job, obj.job_list))

    def _apply_defaults_for_SimpleFolder(self, obj: SimpleFolder):
        self._apply_defaults_for_type(obj, 'SimpleFolder')
        list(map(self._apply_defaults_for_job, obj.job_list))

    def _apply_defaults_for_SubFolder(self, obj: SubFolder):
        self._apply_defaults_for_type(obj, 'SubFolder')

    def add(self, obj: AAPIObject, inpath: str = None, allow_creation: bool = True):
        # apply defaults:
        if isinstance(obj, Job):
            self._apply_defaults_for_job(obj)
        elif isinstance(obj, SubFolder):
            self._apply_defaults_for_SubFolder(obj)
        elif isinstance(obj, Folder):
            self._apply_defaults_for_folder(obj)
        elif isinstance(obj, SimpleFolder):
            self._apply_defaults_for_SimpleFolder(obj)
        else:
            pass

        if inpath:
            if isinstance(obj, SubFolder) or isinstance(obj, Job):
                try:
                    folder = self.get(inpath)
                except Exception as e:
                    if allow_creation:
                        folder = None
                    else:
                        raise e
                if folder:
                    if isinstance(obj, Job):
                        folder.job_list.append(obj)
                    else:
                        folder.sub_folder_list.append(obj)
                else:
                    # Folder does not exist, create folder
                    folder, parent_folder = self.create_folder_hierarchy(inpath)
                    self._apply_defaults_for_folder(folder)
                    if isinstance(obj, Job):
                        parent_folder.job_list.append(obj)
                    else:
                        parent_folder.sub_folder_list.append(obj)

                    self._definitions[folder.object_name] = folder
            else:
                raise Exception(
                    f'Cannot add object of type {type(obj)} into Folder. Only SubFolder and Job is allowed')
        else:
            if not (isinstance(obj, SimpleFolder)
                    or isinstance(obj, Folder)
                    or isinstance(obj, ConnectionProfile)
                    ):
                raise Exception(
                    f'Cannot add object of type {type(obj)} as root definition. Only Folder and SimpleFolder is allowed')
            else:
                self._definitions[obj.object_name] = obj

        if inpath:
            return '/'.join([inpath, obj.object_name])
        else:
            return obj.object_name

    def connect(self, srcpath: str, destpath: str, *, inpath: str = None):
        if inpath:
            srcpath = f'{inpath}/{srcpath}'
            destpath = f'{inpath}/{destpath}'

        obj_src = self.get(srcpath)
        obj_dest = self.get(destpath)

        if not isinstance(obj_src, AAPIJob) or not isinstance(obj_dest, AAPIJob):
            raise Exception(
                f'Cannot connect objects of type {type(obj_src)} with {type(obj_dest)}. Connections can be made from/to Folder, SubFolder and Job')

        key_name = (srcpath, destpath)
        event_name = f'{obj_src.object_name.replace(" ", "_")}-TO-{obj_dest.object_name.replace(" ", "_")}'
        if event_name in self._connections:
            self._connections[event_name].append(key_name)
            count = len(self._connections[event_name])+1
            event_name = f'{event_name}-{count}'
        else:
            # self._connections[key_name] = {'count': 1, 'name': event_name}
            self._connections[event_name] = [key_name]

        # Write the add, wait and delete events, support backward compatibility

        if not obj_src.events_to_add and not obj_src.add_events_list:
            obj_src.events_to_add.append(
                AddEvents(events=[]))
        obj_src.events_to_add[-1].events.append(
            EventOutAdd(event=event_name))

        if not obj_dest.wait_for_events and not obj_dest.wait_for_events_list:
            obj_dest.wait_for_events.append(
                WaitForEvents(events=[]))
        obj_dest.wait_for_events[-1].events.append(
            EventIn(event=event_name))

        if not obj_dest.events_to_delete and not obj_dest.delete_events_list:
            obj_dest.events_to_delete.append(
                DeleteEvents(events=[]))
        obj_dest.events_to_delete[-1].events.append(
            EventOutDelete(event=event_name))

    def chain(self, obj_list: typing.List[AAPIJob], inpath: str):
        objpaths = []
        objname = [o.object_name for o in obj_list]
        clct = collections.Counter(objname)
        dupl = []
        for c in clct:
            if clct[c] > 1:
                dupl.append(f'"{c}"')

        if dupl:
            raise Exception(f'Multiple definitions for: {" , ".join(dupl)}')

        objs_paths = []
        for obj in obj_list:
            objs_paths.append(self.add(obj, inpath=inpath))
            objpaths.append(obj.object_name)

        connections = [(objpaths[i], objpaths[i+1])
                       for i, _ in enumerate(objpaths[:-1])]
        for conn in connections:
            self.connect(conn[0], conn[1], inpath=inpath)

        return objs_paths

    def get_objects(self, path: str) -> typing.List[AAPIObject]:
        pathparts = path.split('/')
        name = pathparts[-1]
        pathparts = pathparts[:-1]

        current_object = self._definitions

        for i, p in enumerate(pathparts):
            if isinstance(current_object, dict):
                try:
                    current_object = current_object[p]
                except KeyError as e:
                    raise Exception(f'Path {pathparts[:i]} is invalid')

            elif isinstance(current_object, Folder) or isinstance(current_object, SubFolder):
                try:
                    current_object = [
                        o for o in current_object.sub_folder_list if o.object_name == p][0]
                except IndexError as e:
                    raise Exception(f'Path {pathparts[:i]} is invalid')
            else:
                raise Exception(f'Path {pathparts[:i]} is invalid')

        if isinstance(current_object, dict):
            try:
                res = [current_object[name]]
                return res
            except KeyError as e:
                raise Exception(
                    f'Cannot find object {name} in path: {"/".join(pathparts)}')

        elif isinstance(current_object, Folder) or isinstance(current_object, SubFolder):
            res = [o for o in current_object.sub_folder_list +
                   current_object.job_list if o.object_name == name]
            if not res:
                raise Exception(
                    f'Cannot find object {name} in path: {"/".join(pathparts)}')
            else:
                return res
        elif isinstance(current_object, SimpleFolder):
            res = [o for o in current_object.job_list if o.object_name == name]
            if not res:
                raise Exception(
                    f'Cannot find object {name} in path: {"/".join(pathparts)}')
            else:
                return res
        else:
            raise Exception(
                f'Cannot find object {name} in path: {"/".join(pathparts)}')

    def get(self, path: str, default=None) -> AAPIObject:
        if default is None:
            return self.get_objects(path)[0]
        else:
            try:
                return self.get_objects(path)[0]
            except:
                return default



    def create_folder_hierarchy(self, path : str):
        parts = path.split('/')
        folder = self.get(parts[0], default = Folder(parts[0]))
        parent = folder
        for i,o in enumerate(parts[1:]):
            try:
                subfolder = [sf for sf in parent.sub_folder_list if sf.object_name == o][0]
            except IndexError:
                subfolder = SubFolder(o)
                parent.sub_folder_list.append(subfolder)
            parent = subfolder

        return folder,parent


    def dumps_json(self, indent=None):
        return json.dumps({k: v.as_aapi_dict() for (k, v) in self._definitions.items()}, indent=indent)

    def dump_json(self, f, indent=None):
        return json.dump({k: v.as_aapi_dict() for (k, v) in self._definitions.items()}, f, indent=indent)

    def copy_from(self, workflow):
        self._definitions = copy.deepcopy(workflow._definitions)
        self._connections = copy.deepcopy(workflow._connections)



class Workflow(BaseWorkflow):

    @staticmethod
    def workbench(host : str = 'localhost', port : str = '8443'):
        return Workflow(Environment.create_workbench(host, port), WorkflowDefaults(run_as='workbench'))

    def __init__(self, environment: Environment, defaults: WorkflowDefaults = None, skip_initial_authentication: bool = False) -> None:
        super().__init__(defaults=defaults)

        self.environment = environment

        self.aapiclient: AbstractAAPIClient = None
        if self.environment.mode == EnvironmentMode.SAAS:
            self.aapiclient = SaasAAPIClient(
                environment.endpoint, environment.credentials)
        else:
            self.aapiclient = OnPremAAPIClient(
                environment.endpoint, environment.credentials)

        if not skip_initial_authentication:
            self.authenticate()

    def authenticate(self):
        self.aapiclient.authenticate()

    @sanitize_output
    def build(self, skip_login: bool = False, file_path: str = None, delete_afterwards: bool = True) -> AAPIClientResponse:
        if not skip_login:
            self.aapiclient.authenticate()

        if not file_path:
            file_path = f'{tempfile.gettempdir()}/temp_{random.randint(1000,9999)}.json'

        fpath = pathlib.Path(file_path)

        with open(fpath.resolve(), 'w') as f:
            self.dump_json(f)

        try:
            res = self.aapiclient.build_api.build_file(fpath.resolve())
            return res
        except Exception as e:
            raise e
        finally:
            if delete_afterwards:
                fpath.unlink()

    @sanitize_output
    def deploy(self, skip_login: bool = False, file_path: str = None, delete_afterwards: bool = True) -> AAPIClientResponse:
        if not skip_login:
            self.aapiclient.authenticate()

        if not file_path:
            file_path = f'{tempfile.gettempdir()}/temp_{random.randint(1000,9999)}.json'

        fpath = pathlib.Path(file_path)

        with open(fpath.resolve(), 'w') as f:
            self.dump_json(f)

        try:
            res = self.aapiclient.deploy_api.deploy_file(fpath.resolve())
            return res
        except Exception as e:
            raise e
        finally:
            if delete_afterwards:
                fpath.unlink()

    # @sanitize_output
    def run(self, skip_login: bool = False, file_path: str = None, delete_afterwards: bool = True, open_in_browser=False) -> RunMonitor:
        if not skip_login:
            self.aapiclient.authenticate()

        if not file_path:
            file_path = f'{tempfile.gettempdir()}/temp_{random.randint(1000,9999)}.json'

        fpath = pathlib.Path(file_path)

        with open(fpath.resolve(), 'w') as f:
            self.dump_json(f)

        try:
            res = self.aapiclient.run_api.run_jobs(fpath.resolve())
            # return res
            run_ =  RunMonitor(res.run_id, self.aapiclient, monitor_page_uri= res.monitor_page_uri)
            if open_in_browser:                
                run_.open_in_browser()
            return run_
        except Exception as e:
            raise e
        finally:
            if delete_afterwards:
                fpath.unlink()
