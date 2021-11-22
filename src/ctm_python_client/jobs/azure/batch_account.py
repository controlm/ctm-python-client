from ctm_python_client.core.base import BaseJob


class BatchAccountJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        job_id,
        command_line,
        append_log,
        wallclock,
        max_tries,
        retention,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.job_id = job_id
        self.command_line = command_line
        self.append_log = append_log
        self.wallclock = wallclock
        self.max_tries = max_tries
        self.retention = retention

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Azure:BatchAccount"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.job_id != None:
            job_json["JobId"] = self.job_id
        if self.command_line != None:
            job_json["CommandLine"] = self.command_line
        if self.append_log != None:
            job_json["AppendLog"] = self.append_log
        if self.wallclock != None:
            job_json["Wallclock"] = self.wallclock
        if self.max_tries != None:
            job_json["MaxTries"] = self.max_tries
        if self.retention != None:
            job_json["Retention"] = self.retention
        return job_json
