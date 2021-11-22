from ctm_python_client.core.base import BaseJob


class StepFunctionJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        state_machine,
        execution_name,
        input,        
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.state_machine = state_machine
        self.execution_name = execution_name
        self.input = input        

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:AWS:StepFunction"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.state_machine != None:
            job_json["StateMachine"] = self.state_machine
        if self.execution_name != None:
            job_json["ExecutionName"] = self.execution_name
        if self.input != None:
            job_json["Input"] = self.input
        return job_json
