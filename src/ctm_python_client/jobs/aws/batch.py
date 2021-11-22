from ctm_python_client.core.base import BaseJob


class BatchJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        job_definition,
        job_definition_revision,
        job_queue,
        aws_job_type,
        array_size,
        depends_on,
        command,
        memory,
        v_c_p_us,
        job_attempts,
        execution_timeout,
        append_log,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.job_name = job_name
        self.job_definition = job_definition
        self.job_definition_revision = job_definition_revision
        self.job_queue = job_queue
        self.aws_job_type = aws_job_type
        self.array_size = array_size
        self.depends_on = depends_on
        self.command = command
        self.memory = memory
        self.v_c_p_us = v_c_p_us
        self.job_attempts = job_attempts
        self.execution_timeout = execution_timeout
        self.append_log = append_log

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:AWS:Batch"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.job_name != None:
            job_json["JobName"] = self.job_name
        if self.job_definition != None:
            job_json["JobDefinition"] = self.job_definition
        if self.job_definition_revision != None:
            job_json["JobDefinitionRevision"] = self.job_definition_revision
        if self.job_queue != None:
            job_json["JobQueue"] = self.job_queue
        if self.aws_job_type != None:
            job_json["AWSJobType"] = self.aws_job_type
        if self.array_size != None:
            job_json["ArraySize"] = self.array_size
        if self.depends_on != None:
            job_json["DependsOn"] = self.depends_on
        if self.command != None:
            job_json["Command"] = self.command
        if self.memory != None:
            job_json["Memory"] = self.memory
        if self.v_c_p_us != None:
            job_json["vCPUs"] = self.v_c_p_us
        if self.job_attempts != None:
            job_json["JobAttempts"] = self.job_attempts
        if self.execution_timeout != None:
            job_json["ExecutionTimeout"] = self.execution_timeout
        if self.append_log != None:
            job_json["AppendLog"] = self.append_log
        return job_json
