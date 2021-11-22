from ctm_python_client.core.base import BaseJob


class TajoQueryJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        open_query,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.open_query = open_query

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Tajo:Query"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.open_query != None:
            job_json["OpenQuery"] = self.open_query
        return job_json
