# Demo: Defining Control_M Workflows using Python

# Step 1 - Setup

## Step 1A - Install the library

# Make sure you have installed the library
# pip install git+https://github.com/controlm/ctm-python-client.git')

from ctm_python_client.core.bmc_control_m import CmJobFlow
from ctm_python_client.jobs.dummy import DummyJob

from ctm_python_client.session.session import Session
import getpass
# Uncomment the section you want to use:

# If using user/password authentication:
# ctm_user = 'EnterUserName'
# endpoint = 'https://<your endpoint>:8443/automation-api'
# password = getpass.getpass('Enter password for {}:'.format(username))

# If using api key authentication:
# endpoint = 'https://<your endpoint>:8443/automation-api'
# api_key = getpass.getpass('Enter api key:')

# If using user/password authentication:
#session = Session(endpoint=endpoint, username=ctm_user, password=ctm_pwd)

# If using api key authentication:
#session = Session(endpoint=endpoint, api_key=api_key)


## Step 2B - Create the object

from ctm_python_client.session.session import Session

#session = Session(endpoint=ctm_uri, username=ctm_user, password=ctm_pwd)
session = Session(endpoint=endpoint, username=ctm_user, password=password)
session.get_token()


t1_flow = CmJobFlow( application="Demo", sub_application="HelloWorld", session=session)


## Step 2C - Define the Schedule


t1_flow.set_run_as(username="ctmuser", host="agent-host")



# Define the schedule
months = ["JAN", "OCT", "DEC"]
monthDays = ["ALL"]
weekDays = ["MON", "TUE", "WED", "THU", "FRI"]
fromTime = "0300"
toTime = "2100"
t1_flow.set_schedule(months, monthDays, weekDays, fromTime, toTime)


# Step 3  - Create Folder



# Create Fodler
f1 = t1_flow.create_folder(name="HelloWorld")


# Step 4 - Create Tasks



start = t1_flow.add_job(f1, DummyJob(f1, "Start-Flow"))
end = t1_flow.add_job(f1, DummyJob(f1, "End-Flow"))

hello_world_id = t1_flow.add_job(f1, DummyJob(f1, "Hello-World"))


# Step 5 - Chain Tasks



# start >>  hello_world_id >> end
t1_flow.chain_jobs(f1, [start, hello_world_id, end])


# Step 6 - Display Workflow

## Step 6A - Display JSON
t1_flow.display_json()


# Step 7 - Submit Workflow to Control-M

t1_flow.deploy()


t1_flow.run()





