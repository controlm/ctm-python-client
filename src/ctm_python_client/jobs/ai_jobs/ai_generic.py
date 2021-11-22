from ctm_python_client.core.base import BaseJob


class AiGenericJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        ai_name,
        host=None,
        run_as=None,
        description=None,
        **kwargs
    ):
        BaseJob.__init__(self, folder, job_name, description, host, run_as)
        self.connection_profile = connection_profile
        self.ai_name = ai_name
        self.ai_params = kwargs

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:ApplicationIntegrator:" + self.ai_name
        job_json["ConnectionProfile"] = self.connection_profile
        for key, value in self.ai_params.items():
            job_json[key] = value
        return job_json
