from ctm_python_client.core.base import BaseJob


class AgentJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        category,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.job_name = job_name
        self.category = category

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Database:MSSQL:AgentJob"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.job_name != None:
            job_json["JobName"] = self.job_name
        if self.category != None:
            job_json["Category"] = self.category
        return job_json
