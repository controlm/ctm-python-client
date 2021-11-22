from ctm_python_client.core.base import BaseJob


class ScalaJavaJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        program_jar,
        main_class,
        arguments,
        pre_commands,
        post_commands,
        spark_options,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.program_jar = program_jar
        self.main_class = main_class
        self.arguments = arguments
        self.pre_commands = pre_commands
        self.post_commands = post_commands
        self.spark_options = spark_options

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Hadoop:Spark:ScalaJava"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.program_jar != None:
            job_json["ProgramJar"] = self.program_jar
        if self.main_class != None:
            job_json["MainClass"] = self.main_class
        if self.arguments != None:
            job_json["Arguments"] = self.arguments
        if self.pre_commands != None:
            job_json["PreCommands"] = self.pre_commands
        if self.post_commands != None:
            job_json["PostCommands"] = self.post_commands
        if self.spark_options != None:
            job_json["SparkOptions"] = self.spark_options
        return job_json
