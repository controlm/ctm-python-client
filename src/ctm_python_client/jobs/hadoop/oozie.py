from ctm_python_client.core.base import BaseJob


class OozieJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        job_properties_file,
        oozie_options,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.job_properties_file = job_properties_file
        self.oozie_options = oozie_options

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Oozie"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.job_properties_file != None:
            job_json["JobPropertiesFile"] = self.job_properties_file
        if self.oozie_options != None:
            job_json["OozieOptions"] = self.oozie_options
        return job_json
