from ctm_python_client.core.base import BaseJob


class SSISJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        package_source,
        package_name,
        config_files,
        properties,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.package_source = package_source
        self.package_name = package_name
        self.config_files = config_files
        self.properties = properties

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Database:MSSQL:SSIS"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.package_source != None:
            job_json["PackageSource"] = self.package_source
        if self.package_name != None:
            job_json["PackageName"] = self.package_name
        if self.config_files != None:
            job_json["ConfigFiles"] = self.config_files
        if self.properties != None:
            job_json["Properties"] = self.properties
        return job_json
