from ctm_python_client.core.base import BaseJob


class MapredStreamingJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        input_path,
        output_path,
        mapper_command,
        reducer_command,
        general_options,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.input_path = input_path
        self.output_path = output_path
        self.mapper_command = mapper_command
        self.reducer_command = reducer_command
        self.general_options = general_options

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:MapredStreaming"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.input_path != None:
            job_json["InputPath"] = self.input_path
        if self.output_path != None:
            job_json["OutputPath"] = self.output_path
        if self.mapper_command != None:
            job_json["MapperCommand"] = self.mapper_command
        if self.reducer_command != None:
            job_json["ReducerCommand"] = self.reducer_command
        if self.general_options != None:
            job_json["GeneralOptions"] = self.general_options
        return job_json
