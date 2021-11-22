from ctm_python_client.core.base import BaseJob


class HDFSCommandsJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        commands,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.commands = commands

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:HDFSCommands"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.commands != None:
            job_json["Commands"] = self.commands
        return job_json
