from ctm_python_client.core.base import BaseJob


class DummyJob(BaseJob):
    def __init__(self, folder, job_name, host=None, run_as=None, description=None):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:Dummy"
        return job_json
