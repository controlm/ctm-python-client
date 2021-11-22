from ctm_python_client.core.base import BaseJob


class HiveJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        hive_script,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.hive_script = hive_script

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Hive"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.hive_script != None:
            job_json["HiveScript"] = self.hive_script
        return job_json
