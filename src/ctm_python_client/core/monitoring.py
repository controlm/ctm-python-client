from clients import ctm_api_client
from ctm_python_client.core.comm import AbstractAAPIClient, OnPremAAPIClient

import webbrowser


__all__ = ['RunMonitor']


class RunMonitor:
    '''
    Class RunMonitor

    Allows basic monitoring functions in a similar way that found in the Control-M Web interface
    '''

    def __init__(self, run_id: str, aapiclient: OnPremAAPIClient, monitor_page_uri: str = None) -> None:
        self.run_id = run_id
        self.monitor_page_uri = monitor_page_uri
        self.aapiclient = aapiclient

    def get_statuses(self):
        '''
        Get the status of the run and all its jobs
        '''
        try:
            res = self.aapiclient.run_api.get_jobs_status(self.run_id)
            return res.statuses
        except Exception as e:
            raise e

    @staticmethod
    def _pretty_print_statuses(statuses):
        print('Run Status')
        print('-'*50)
        for status in statuses:
            # print(f'{status.type} "{status.name}" ({status.folder}) - {status.status}')
            if status.folder:
                idnt = status.folder.count('/')+1
            else:
                idnt = 0
            print(f'{"    "*idnt + status.name+"  " :.<40}  {status.status}')

        print('')

    def print_statuses(self, **kwargs):
        '''
        Pretty prints full status of the run and all its jobs

        You can pass printer kwarg to specify a pretty pritner function. The function accepts one argument: the list of statuses
        '''
        if kwargs.get('printer'):
            printer = kwargs.get('printer')

        else:
            printer = self._pretty_print_statuses

        return printer(self.get_statuses())

    def get_status(self, job_name: str):
        '''
        Get the status of a job.       
        '''
        job_id = self.get_jobid(job_name)
        try:
            res = self.aapiclient.run_api.get_jobs_status(self.run_id)
            return [
                o for o in res.statuses if o.job_id == job_id
            ][0]
        except Exception as e:
            if isinstance(e, IndexError):
                raise Exception(
                    f'Cannot get status for {job_name}')
            raise e

    def get_output(self, job_name: str) -> str:
        '''
        Get the output of a job describing all actions regarding the job execution.
        If not applicable, it returns None.        
        '''

        job_id = self.get_jobid(job_name)

        try:
            res = self.aapiclient.run_api.get_job_output(job_id=job_id)
            return res
        except Exception as e:
            if isinstance(e, IndexError):
                raise Exception(f'Cannot get output for {job_name}')
            elif 'OUTPUT DOES NOT EXIST FOR THIS JOB' in e.body:
                return None
            raise e

    def print_output(self, job_name: str):
        '''
        Print the output of a job describing all actions regarding the job execution.

        '''
        print(self.get_output(job_name))

    def get_log(self, job_name: str) -> str:
        '''
        Get the log of a job describing all actions regarding the job execution.            
        '''

        job_id = self.get_jobid(job_name)

        try:
            res = self.aapiclient.run_api.get_job_log(job_id=job_id)
            return res
        except Exception as e:
            if isinstance(e, IndexError):
                raise Exception(f'Cannot get log for {job_name}')
            raise e

    def confirm_job(self, job_name: str) -> str:
        '''
        Confirms a job. This only applies to jobs which where defined with `confirm=True`.
        Trying to confirm a job which can't be confirmed or was already confirmed will result in error
        '''
        job_id = self.get_jobid(job_name)

        try:
            res = self.aapiclient.run_api.confirm_job(job_id=job_id)
            if 'confirmed' in res.message:
                return f'Job {job_name} ({job_id}) confirmed by user'
        except Exception as e:
            if isinstance(e, IndexError):
                raise Exception(f'Cannot confirm {job_name}')
            raise e

    def get_jobid(self, job_name: str) -> str:
        '''
        Get the job id from a job_name. 

        job_name can be a job name with or without path.
        If there are multiple jobs with the same name, the result will be determined according to path
        If no path is given, there will be an undefined behavior.

        job_name example : "MyJob" or with path: "MyFolder/Subfolder1/Subfolder2/MyJob"
        '''
        parts = job_name.split('/')
        inpath = '/'.join(parts[:-1])
        job_name = parts[-1]

        def cond(o):
            if o.name != job_name:
                return False
            if inpath:
                return o.folder == inpath
            else:
                return True

        try:
            res = self.aapiclient.run_api.get_jobs_status(self.run_id)
            return [
                o for o in res.statuses if cond(o)
            ][0].job_id
        except Exception as e:
            if isinstance(e, IndexError):
                raise Exception(f'Cannot get job_id for {job_name}')
            raise e

    def open_in_browser(self):
        if self.monitor_page_uri is None:
            raise Exception(
                'This operation is not supported in this environment')

        webbrowser.open(self.monitor_page_uri, 0)
