from setuptools import find_packages, setup

setup(
    name="ctm-python-client",
    packages=find_packages(where="src"),    
    package_dir={"": "src"},
    version="1.0.0",
    description="Python Workflows for Control-M",
    author="BMC Software",
    license="BSD 2-Clause",
    install_requires=["graphviz>=0.10", "requests>=2.23.0", "urllib3", "six"],
)