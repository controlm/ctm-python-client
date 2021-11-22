from ctm_python_client.core.base import BaseJob


class PeopleSoftJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        user,
        control_id,
        server_name,
        process_type,
        process_name,
        append_to_output,
        bind_variables,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.user = user
        self.control_id = control_id
        self.server_name = server_name
        self.process_type = process_type
        self.process_name = process_name
        self.append_to_output = append_to_output
        self.bind_variables = bind_variables

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:PeopleSoft"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.user != None:
            job_json["User"] = self.user
        if self.control_id != None:
            job_json["ControlId"] = self.control_id
        if self.server_name != None:
            job_json["ServerName"] = self.server_name
        if self.process_type != None:
            job_json["ProcessType"] = self.process_type
        if self.process_name != None:
            job_json["ProcessName"] = self.process_name
        if self.append_to_output != None:
            job_json["AppendToOutput"] = self.append_to_output
        if self.bind_variables != None:
            job_json["BindVariables"] = self.bind_variables
        return job_json
