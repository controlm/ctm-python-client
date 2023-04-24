# Getting Started

The best way to get to know Control-M Python Client is to follow the [Tutorials](/tutorials).
The tutorials guide you through your first steps of building your workflows. See [Getting Started with Control-M Python Client](/notebooks/hello)

## Environment

To deploy and run jobs from Control-M Python Client, you need access to an active Control-M environment.
If you don't have an active Control-M environment, or you want to test some workflows on a free of cost development platform you can use Control-M Workbench.

We suggest that you download a python IDE. 

## Installation

If you don't have Python, download [Python](https://www.python.org/downloads/)

**Control-M Python Client requires Python version 3.7 or higher**


We recommend to install Control-M Python Client in a [virtual environment](https://docs.python.org/3/library/venv.html). 

Here's how to create a virtual environment:

**UNIX**
```shell
python -m venv venv
source venv/bin/activate
```

**Windows**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### Installing via pip

**Note: Requires `pip` and `git` to be installed.**

```shell
pip install git+https://github.com/controlm/ctm-python-client.git
```

### Installing from source

```shell
git clone https://github.com/controlm/ctm-python-client.git
pip install ctm-python-client
```
