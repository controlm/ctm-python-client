from setuptools import find_packages, setup

setup(
    name="ctm-python-client",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="2.1.0-alpha",
    description="Python Workflows for Control-M",
    author="BMC Software",
    license="BSD 3-Clause",
    install_requires=["requests>=2.23.0",
                      "urllib3", "six", "attrs", "certifi"],
)
