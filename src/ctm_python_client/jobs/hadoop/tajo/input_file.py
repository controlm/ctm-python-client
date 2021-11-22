from ctm_python_client.core.base import BaseJob


class InputFileJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        full_file_path,
        parameters=None,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.full_file_path = full_file_path
        self.parameters = parameters

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Tajo:InputFile"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.full_file_path != None:
            job_json["FullFilePath"] = self.full_file_path
        if self.parameters != None:
            job_json["Parameters"] = self.parameters
        return job_json
