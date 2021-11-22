from ctm_python_client.core.base import BaseJob


class ProcessChainJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        process_chain_description,
        id,
        rerun_option,
        enable_peridoic_job,
        consider_only_overall_chain_status,
        retrieve_log,
        detect_spawned_job,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.process_chain_description = process_chain_description
        self.id = id
        self.rerun_option = rerun_option
        self.enable_peridoic_job = enable_peridoic_job
        self.consider_only_overall_chain_status = consider_only_overall_chain_status
        self.retrieve_log = retrieve_log
        self.detect_spawned_job = detect_spawned_job

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:SAP:BW:ProcessChain"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.process_chain_description != None:
            job_json["ProcessChainDescription"] = self.process_chain_description
        if self.id != None:
            job_json["Id"] = self.id
        if self.rerun_option != None:
            job_json["RerunOption"] = self.rerun_option
        if self.enable_peridoic_job != None:
            job_json["EnablePeridoicJob"] = self.enable_peridoic_job
        if self.consider_only_overall_chain_status != None:
            job_json[
                "ConsiderOnlyOverallChainStatus"
            ] = self.consider_only_overall_chain_status
        if self.retrieve_log != None:
            job_json["RetrieveLog"] = self.retrieve_log
        if self.detect_spawned_job != None:
            job_json["DetectSpawnedJob"] = self.detect_spawned_job
        return job_json
