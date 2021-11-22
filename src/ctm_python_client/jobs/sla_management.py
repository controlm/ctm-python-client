from ctm_python_client.core.base import BaseJob


class SLAManagementJob(BaseJob):
    def __init__(
        self,
        folder,
        job_name,
        service_name,
        service_priority,
        created_by,
        job_runs_deviations_tolerance,
        complete_in,
        events_to_wait_for,
        events_to_delete,
        host=None,
        run_as=None,
        description=None,
    ):

        BaseJob.__init__(
            self, folder, job_name, description=description, host=host, run_as=run_as
        )
        self.service_name = service_name
        self.service_priority = service_priority
        self.created_by = created_by
        self.job_runs_deviations_tolerance = job_runs_deviations_tolerance
        self.complete_in = complete_in
        self.events_to_wait_for = events_to_wait_for
        self.events_to_delete = events_to_delete

    def get_json(self):
        job_json = BaseJob.get_json(self)
        job_json["Type"] = "Job:SLAManagement"
        if self.service_name != None:
            job_json["ServiceName"] = self.service_name
        if self.service_priority != None:
            job_json["ServicePriority"] = self.service_priority
        if self.created_by != None:
            job_json["CreatedBy"] = self.created_by
        if self.job_runs_deviations_tolerance != None:
            job_json["JobRunsDeviationsTolerance"] = self.job_runs_deviations_tolerance
        if self.complete_in != None:
            job_json["CompleteIn"] = self.complete_in
        if self.events_to_wait_for != None:
            job_json["eventsToWaitFor"] = self.events_to_wait_for
        if self.events_to_delete != None:
            job_json["eventsToDelete"] = self.events_to_delete
        return job_json
