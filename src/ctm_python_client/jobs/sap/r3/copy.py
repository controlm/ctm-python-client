from ctm_python_client.core.base import BaseJob


class COPYJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        connection_profile,
        sap_job_name,
        exec,
        target,
        job_count,
        job_count_specific_name,
        new_job_name,
        start_condition,
        after_event,
        after_event_parameters,
        rerun_from_point_of_failure,
        copy_from_step,
        post_job_action,
        detect_spawned_job,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.connection_profile = connection_profile
        self.sap_job_name = sap_job_name
        self.exec = exec
        self.target = target
        self.job_count = job_count
        self.job_count_specific_name = job_count_specific_name
        self.new_job_name = new_job_name
        self.start_condition = start_condition
        self.after_event = after_event
        self.after_event_parameters = after_event_parameters
        self.rerun_from_point_of_failure = rerun_from_point_of_failure
        self.copy_from_step = copy_from_step
        self.post_job_action = post_job_action
        self.detect_spawned_job = detect_spawned_job

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:SAP:R3:COPY"
        if self.connection_profile != None:
            job_json["ConnectionProfile"] = self.connection_profile
        if self.sap_job_name != None:
            job_json["SapJobName"] = self.sap_job_name
        if self.exec != None:
            job_json["Exec"] = self.exec
        if self.target != None:
            job_json["Target"] = self.target
        if self.job_count != None:
            job_json["JobCount"] = self.job_count
        if self.job_count_specific_name != None:
            job_json["JobCountSpecificName"] = self.job_count_specific_name
        if self.new_job_name != None:
            job_json["NewJobName"] = self.new_job_name
        if self.start_condition != None:
            job_json["StartCondition"] = self.start_condition
        if self.after_event != None:
            job_json["AfterEvent"] = self.after_event
        if self.after_event_parameters != None:
            job_json["AfterEventParameters"] = self.after_event_parameters
        if self.rerun_from_point_of_failure != None:
            job_json["RerunFromPointOfFailure"] = self.rerun_from_point_of_failure
        if self.copy_from_step != None:
            job_json["CopyFromStep"] = self.copy_from_step
        if self.post_job_action != None:
            job_json["PostJobAction"] = self.post_job_action
        if self.detect_spawned_job != None:
            job_json["DetectSpawnedJob"] = self.detect_spawned_job
        return job_json
