from ctm_python_client.core.base import BaseJob


# class InformaticaJob(BaseJob):
#     def __init__(
#         self,
#         folder,
#         job_name,
#         connection_profile,
#         repository_folder,
#         workflow,
#         workflow_execution_mode,
#         workflow_restart_mode,
#         enable_output,
#         enable_error_details,
#         priority,
#         instance_name=None,
#         os_profile = None,
#         host=None,
#         run_as=None,
#         description=None,
#     ):
#         BaseJob.__init__(self, folder, job_name, description, host, run_as)
#         self.connection_profile = connection_profile
#         self.repository_folder = repository_folder
#         self.workflow = workflow
#         self.workflow_execution_mode = workflow_execution_mode
#         self.workflow_restart_mode = workflow_restart_mode
#         self.enable_output = enable_output
#         self.enable_error_details = enable_error_details
#         self.priority = priority
#         self.instance_name = instance_name
#         self.os_profile = os_profile


#     def get_json(self):
#         job_json = BaseJob.get_json(self)
#         job_json["Type"] = "Job:Informatica"
#         job_json["ConnectionProfile"] = self.connection_profile
#         job_json["RepositoryFolder"] = self.repository_folder
#         job_json["Workflow"] = self.workflow
#         job_json["WorkflowExecutionMode"] = self.workflow_execution_mode
#         job_json["WorkflowRestartMode"] = self.workflow_restart_mode
#         job_json["EnableOutput"] = self.enable_output
#         job_json["EnableErrorDetails"] = self.enable_error_details
#         job_json["Priority"] = self.priority
#         if self.instance_name != None:
#             job_json["InstanceName"] = self.instance_name
#         if self.os_profile != None:
#             job_json["OsProfile"] = self.os_profile
#         return job_json


class InformaticaJob(BaseJob):
	def __init__(self, folder, job_name,
				connection_profile,
				repository_folder,
				workflow,
				instance_name=None,
				os_profile=None,
				workflow_execution_mode=None,
				run_single_task=None,
				workflow_restart_mode=None,
				restart_from_task=None,
				workflow_parameters_file=None,
				host=None, run_as=None, description=None):

		BaseJob.__init__(self, folder, job_name, description=description, host=host, run_as=run_as)
		self.connection_profile = connection_profile
		self.repository_folder = repository_folder
		self.workflow = workflow
		self.instance_name = instance_name
		self.os_profile = os_profile
		self.workflow_execution_mode = workflow_execution_mode
		self.run_single_task = run_single_task
		self.workflow_restart_mode = workflow_restart_mode
		self.restart_from_task = restart_from_task
		self.workflow_parameters_file = workflow_parameters_file

	def get_json(self):
		job_json = BaseJob.get_json(self)
		job_json['Type'] = 'Job:Informatica'
		if self.connection_profile != None:
			job_json['ConnectionProfile'] = self.connection_profile
		if self.repository_folder != None:
			job_json['RepositoryFolder'] = self.repository_folder
		if self.workflow != None:
			job_json['Workflow'] = self.workflow
		if self.instance_name != None:
			job_json['InstanceName'] = self.instance_name
		if self.os_profile != None:
			job_json['OsProfile'] = self.os_profile
		if self.workflow_execution_mode != None:
			job_json['WorkflowExecutionMode'] = self.workflow_execution_mode
		if self.run_single_task != None:
			job_json['RunSingleTask'] = self.run_single_task
		if self.workflow_restart_mode != None:
			job_json['WorkflowRestartMode'] = self.workflow_restart_mode
		if self.restart_from_task != None:
			job_json['RestartFromTask'] = self.restart_from_task
		if self.workflow_parameters_file != None:
			job_json['WorkflowParametersFile'] = self.workflow_parameters_file
		return job_json
