from ctm_python_client.core.base import BaseJob


class DistCpJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        target_path,
        source_paths,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.target_path = target_path
        self.source_paths = source_paths

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:DistCp"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.target_path != None:
            job_json["TargetPath"] = self.target_path
        if self.source_paths != None:
            job_json["SourcePaths"] = self.source_paths
        return job_json
