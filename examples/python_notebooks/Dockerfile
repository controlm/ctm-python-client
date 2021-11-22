# This Dockerfile, creates a jupyter notebook environment and install controlm_python_client 
# so the example notebooks or any other notebooks that the users would like to work with
#
FROM jupyter/base-notebook:python-3.8.3

USER root
RUN apt-get -y update
RUN apt install -y git
RUN apt install -y graphviz
RUN pip install --upgrade pip

# this installs the controlm_python_client
RUN pip  install git+https://github.com/tadinve/ctm_python_client.git
CMD /bin/bash