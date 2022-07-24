from setuptools import find_packages, setup
import sys
sys.path.append('src')
import ctm_python_client

setup(
    name="ctm-python-client",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version=ctm_python_client.__version__,
    description="Python Workflows for Control-M",
    author=ctm_python_client.__author__,
    license="BSD 3-Clause",
    install_requires=["requests>=2.23.0",
                      "urllib3", "six", "attrs", "certifi"],
)
