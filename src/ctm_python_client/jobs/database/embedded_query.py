from ctm_python_client.core.base import BaseJob


class EmbeddedQueryJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        query,
        variables=None,
        output_execution_log=None,
        autocommit=None,
        output_sql_output=None,
        sql_output_format=None,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.query = query
        self.variables = variables
        self.output_execution_log = output_execution_log
        self.autocommit = autocommit
        self.output_sql_output = output_sql_output
        self.sql_output_format = sql_output_format

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Database:EmbeddedQuery"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.query != None:
            job_json["Query"] = self.query
        if self.variables != None:
            job_json["Variables"] = self.variables
        if self.output_execution_log != None:
            job_json["OutputExecutionLog"] = self.output_execution_log
        if self.autocommit != None:
            job_json["Autocommit"] = self.autocommit
        if self.output_sql_output != None:
            job_json["OutputSQLOutput"] = self.output_sql_output
        if self.sql_output_format != None:
            job_json["SQLOutputFormat"] = self.sql_output_format
        return job_json
