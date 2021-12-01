# How to contribute to Control-M Python Client

## Reporting bugs and opening issues

If you have found any bug, check if there is not already an [issue opened](https://github.com/controlm/ctm-python-client/issues) on it. If none are opened on the subject, you can create a new one


## Contributions

To contribute, you should fork the project and open a [pull request](https://github.com/controlm/ctm-python-client/pulls)

Before opening a pull request make sure another one on the same subject is not opened already

### Setting up a development environment

Use the `requirements_dev.txt`

```
$ git clone https://github.com/controlm/ctm-python-client.git
$ cd ctm-python-client
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements_dev.txt

```

### Guidelines

Examples ares structured in folders with relevant files and data in it. If your example uses scripts or other resources, add it in the folder. Do not store any real data or sensitive information! If you contribute with notebooks, clean the output before committing

Example `101-HelloWorld` should always be first in the list

Note: The folders `ctm_api_client` and `ctm_saas_client` only contains generated code and should not be modified. Check `ctm_python_client` for the interesting stuff
