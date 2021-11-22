from ctm_python_client.core.base import BaseJob


class DeleteJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        path,
        search_interval,
        time_limit,
        start_time,
        stop_time,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.path = path
        self.search_interval = search_interval
        self.time_limit = time_limit
        self.start_time = start_time
        self.stop_time = stop_time

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:FileWatcher:Delete"
        if self.path != None:
            job_json["Path"] = self.path
        if self.search_interval != None:
            job_json["SearchInterval"] = self.search_interval
        if self.time_limit != None:
            job_json["TimeLimit"] = self.time_limit
        if self.start_time != None:
            job_json["StartTime"] = self.start_time
        if self.stop_time != None:
            job_json["StopTime"] = self.stop_time
        return job_json
