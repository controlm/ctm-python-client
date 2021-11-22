from ctm_python_client.core.base import BaseJob


class SqoopJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        sqoop_command,
        sqoop_options,
        sqoop_archives,
        sqoop_files,
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
        self.sqoop_command = sqoop_command
        self.sqoop_options = sqoop_options
        self.sqoop_archives = sqoop_archives
        self.sqoop_files = sqoop_files
        self.pre_commands = pre_commands
        self.post_commands = post_commands

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Sqoop"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.sqoop_command != None:
            job_json["SqoopCommand"] = self.sqoop_command
        if self.sqoop_options != None:
            job_json["SqoopOptions"] = self.sqoop_options
        if self.sqoop_archives != None:
            job_json["SqoopArchives"] = self.sqoop_archives
        if self.sqoop_files != None:
            job_json["SqoopFiles"] = self.sqoop_files
        if self.pre_commands != None:
            job_json["PreCommands"] = self.pre_commands
        if self.post_commands != None:
            job_json["PostCommands"] = self.post_commands
        return job_json
