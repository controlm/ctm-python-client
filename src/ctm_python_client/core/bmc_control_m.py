import os
import json
from ctm_python_client.session.session import Session
from clients import ctm_api_client, ctm_saas_client
import logging


JOBS_FILE = "jobs.json"


class CmJobFlow:

    # Constructor and setting some default values
    def __init__(
        self,
        application,
        sub_application,
        ctm_uri = None,
        description=None,
        order_method=None,
        session=None,
        debug = False,
    ):
        self.application = application
        self.sub_application = sub_application
        self.folders = []
        self.jobs = []
        self.run_as_set = False
        self.schedule_set = False
        self.failure_notification = False
        if session != None:
            self.uri = session.endpoint
        else:
            self.uri = None

        if debug:
            logging.basicConfig(level=logging.DEBUG)

        # session variables
        self.session = session


        # network graph
        self.nodes = []
        self.edges = []

        self.flowcount = 0
        self.variables = []

        self.json = {
            "Defaults": {"Application": application, "SubApplication": sub_application}
        }
        if description is not None:
            self.json["Defaults"]["Description"] = description
        if order_method is not None:
            self.json["Defaults"]["OrderMethod"] = order_method

        # Attributes used in methods
        self.token = None
        self.https = None
        self.username = None
        self.host = None
        self.schedule = None
        self.mail_to = None
        self.mail_subject = None


    # this is a private functions defined to create nodes in the graph
    def _create_node(self, name, job):
        self.jobs.append((name, job))
        node_id = str(len(self.jobs) - 1)
        return node_id

    # sets up the default user to run the jobs (can be overridden at the job level)
    def set_run_as(self, username, host, ctm_server=None, site_standard=None, business_fields=None):
        self.run_as_set = True
        self.username = username
        self.host = host
        self.json["Defaults"]["RunAs"] = username
        self.json["Defaults"]["Host"] = host
        if ctm_server is not None:
            self.json["Defaults"]["ControlmServer"] = ctm_server
        if site_standard is not None:
            self.json["Defaults"]["SiteStandard"] = site_standard
        if business_fields is not None:
            self.json["Defaults"]["BusinessFields"] = business_fields

    # sets up the default user to run the jobs (can be overridden at the job level)
    def set_schedule(
                    self, months=None, month_days=None, week_days=None, 
                    from_time=None, to_time=None ):
        self.schedule_set = True
        self.json["Defaults"]["When"] = {}
        if months is not None:
            self.json["Defaults"]["When"]["Months"] = months
        if month_days is not None:
            self.json["Defaults"]["When"]["MonthDays"] = month_days
        if week_days is not None:
            self.json["Defaults"]["When"]["WeekDays"] = week_days
        if from_time is not None:
            self.json["Defaults"]["When"]["FromTime"] = from_time
        if to_time is not None:
            self.json["Defaults"]["When"]["ToTime"] = to_time

    # Whom to email on any job failure
    def set_on_failure_notification(self, mail_to, mail_subject):
        self.failure_notification = True
        self.mail_to = mail_to
        self.mail_subject = mail_subject

    def __str__(self):
        return json.dumps(self.json, indent=4)

    def deploy(self):

        self.deploy_api = self.session.deploy_api
        #self.token = self.session.get_token()

        with open(JOBS_FILE, "w") as outfile:
            json.dump(self.json, outfile, indent=4)

        try:
            result = self.deploy_api.deploy_file(JOBS_FILE)
            logging.debug(result)

        except Exception as e:
            print("Error deploying job, look for more details below")
            print(e)
            return 400 #failure code

        # Remove temporary file
        os.remove(JOBS_FILE)

        print("\n\nSuccessfully deployed to Control-M")
        self.display()
        print("Login to {0}/ControlM/ and use your workflow".format(self.session.format_endpoint()))
        return result

    def run(self):

        self.run_api = self.session.run_api

        #self.token = self.session.get_token()

        with open(JOBS_FILE, "w") as outfile:
            json.dump(self.json, outfile, indent=4)

        try:
            result = self.run_api.run_jobs(JOBS_FILE)
            logging.debug(result)
        except Exception as e:
            print("Error running job, look for more details below")
            print(e)
            return 400

        print("\n\nSuccessfully Ran job on Control-M")
        self.display()
        print("Login to {0}/ControlM/ and use your workflow".format(self.session.format_endpoint()))
        return result



    # This function displays the Jobflow
    def display(self):
        print("\tApplication: ", self.application)
        print("\tSub Application: ", self.sub_application)
        for folder in self.folders:
            print( "\tFolder Name: ", folder[0])

        return True

    def get_json(self):
        json_str = json.dumps(self.json, indent=4)
        return json_str

    def display_json(self):
        json_str = self.get_json()
        print(json_str)

    # Jobs can be grouped together as folders, this creates the folder
    def create_folder(self, name, server=None):
        self.folders.append([name, server])
        self.json[name] = {"Type": "Folder"}
        return name

    # sets up the default user to run the jobs (can be overridden at the job level)
    def add_variables(self, folder, list_of_variables):
        self.variables += list_of_variables
        self.json[folder]["Variables"] = self.variables

    def add_job(self, folder, job):
        job_name = job.get_job_name()
        self.json[folder][job_name] = job.get_json()
        return self._create_node(job_name, job)



    # this function sets up dependencies of jobs, and used to define job execution sequence.
    def chain_jobs(self, folder, links, style="solid"):
        logging.debug(self.jobs)
        logging.debug(links)
        self.flowcount += 1

        from_job = links[0]
        seq = [
            self.jobs[int(links[0])][0],
        ]
        for j in links[1:]:
            self.edges.append(
                (self.jobs[int(from_job)][0], self.jobs[int(j)][0], style)
            )
            seq.append(self.jobs[int(j)][0])
            fj = self.jobs[int(from_job)][1]
            fj.event_to_add(self.jobs[int(j)][0])
            from_job = j

        self.json[folder]["Flow" + str(self.flowcount)] = {
            "Type": "Flow",
            "Sequence": seq,
        }

    # return nodes and edges. can be used by graphviz or matplotlib for display
    def get_nodes_and_edges(self):
        return self.jobs, self.edges
