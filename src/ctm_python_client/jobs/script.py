from ctm_python_client.core.base import BaseJob


class ScriptJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        file_name,
        file_path,
        pre_command,
        post_command,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.file_name = file_name
        self.file_path = file_path
        self.pre_command = pre_command
        self.post_command = post_command

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Script"
        if self.file_name != None:
            job_json["FileName"] = self.file_name
        if self.file_path != None:
            job_json["FilePath"] = self.file_path
        if self.pre_command != None:
            job_json["PreCommand"] = self.pre_command
        if self.post_command != None:
            job_json["PostCommand"] = self.post_command
        return job_json
