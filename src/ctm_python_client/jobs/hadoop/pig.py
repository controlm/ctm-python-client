from ctm_python_client.core.base import BaseJob


class PigJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        pig_script,
        parameters,
        pre_commands,
        post_commands,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.pig_script = pig_script
        self.parameters = parameters
        self.pre_commands = pre_commands
        self.post_commands = post_commands

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Pig"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.pig_script != None:
            job_json["PigScript"] = self.pig_script
        if self.parameters != None:
            job_json["Parameters"] = self.parameters
        if self.pre_commands != None:
            job_json["PreCommands"] = self.pre_commands
        if self.post_commands != None:
            job_json["PostCommands"] = self.post_commands
        return job_json
