from ctm_python_client.core.base import BaseJob


class R3CREATEJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        sap_job_name,
        start_condition,
        rerun_from_step,
        target,
        created_by,
        steps,
        post_job_action,
        spool_list_recipient,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.sap_job_name = sap_job_name
        self.start_condition = start_condition
        self.rerun_from_step = rerun_from_step
        self.target = target
        self.created_by = created_by
        self.steps = steps
        self.post_job_action = post_job_action
        self.spool_list_recipient = spool_list_recipient

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:SAP:R3:CREATE"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.sap_job_name != None:
            job_json["SapJobName"] = self.sap_job_name
        if self.start_condition != None:
            job_json["StartCondition"] = self.start_condition
        if self.rerun_from_step != None:
            job_json["RerunFromStep"] = self.rerun_from_step
        if self.target != None:
            job_json["Target"] = self.target
        if self.created_by != None:
            job_json["CreatedBy"] = self.created_by
        if self.steps != None:
            job_json["Steps"] = self.steps
        if self.post_job_action != None:
            job_json["PostJobAction"] = self.post_job_action
        if self.spool_list_recipient != None:
            job_json["SpoolListRecipient"] = self.spool_list_recipient
        return job_json
