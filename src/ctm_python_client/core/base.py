class BaseJob:
    """
    Abstract class to be derived for jobs. Jobs are processing items with state
    and duration that aren't task instances. For instance a CommandJob is
    a collection of task instance runs, but should have its own state, start
    and end time.
    """

    def __init__(self, folder, job_name, description=None, host=None, run_as=None):
        self.folder = folder
        self.job_name = job_name
        self.host = host
        self.run_as = run_as
        self.capture_count = 0
        self.job_json = {
            "Type": None
        }  # This will be overriden in the inhereted class. S
        self.description = description
        if self.host is not None:
            self.job_json["Host"] = self.host
        if self.run_as is not None:
            self.job_json["RunAs"] = self.run_as
        if self.description is not None:
            self.job_json["Description"] = self.description

    def get_job_name(self):
        return self.job_name

    def get_folder(self):
        return self.folder

    def get_json(self):
        return self.job_json

    def on_success_send_mail(self, mail_subject, mail_to, mail_message):
        self.job_json["OnSuccessMail"] = {
            "Type": "If:CompletionStatus",
            "CompletionStatus": "OK",
            "Mail_0": {
                "Type": "Action:Mail",
                "Subject": mail_subject,
                "To": mail_to,
                "Message": mail_message,
            },
        }

    def capture_output(self, variable, capture_type, search_string):
        self.capture_count += 1
        self.job_json["CaptureOutput_" + str(self.capture_count)] = {
            "Type": "Action:CaptureOutput",
            "Capture": capture_type,
            "Search": search_string,
            "VariableName": "\\\\" + variable,
            "ForwardBy": {"ColumnsOption": "Characters"},
        }

    def set_job_schedule(
        self, months=None, month_days=None, week_days=None, from_time=None, to_time=None
    ):
        self.job_json["When"] = {}
        if months is not None:
            self.job_json["When"]["Months"] = months
        if month_days is not None:
            self.job_json["When"]["MonthDays"] = month_days
        if week_days is not None:
            self.job_json["When"]["WeekDays"] = week_days
        if from_time is not None:
            self.job_json["When"]["FromTime"] = from_time
        if to_time is not None:
            self.job_json["When"]["ToTime"] = to_time

    def event_to_add(self, job_to_name):
        if "eventsToAdd" not in self.job_json:
            self.job_json["eventsToAdd"] = {"Type": "AddEvents", "Events": []}
        self.job_json["eventsToAdd"]["Events"].append(
            {"Event": self.job_name + "-TO-" + job_to_name}
        )


