from ctm_python_client.core.base import BaseJob


class LogicAppsJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        logic_app_name,
        request_body,
        append_log,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.logic_app_name = logic_app_name
        self.request_body = request_body
        self.append_log = append_log

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Azure:LogicApps"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.logic_app_name != None:
            job_json["LogicAppName"] = self.logic_app_name
        if self.request_body != None:
            job_json["RequestBody"] = self.request_body
        if self.append_log != None:
            job_json["AppendLog"] = self.append_log
        return job_json
