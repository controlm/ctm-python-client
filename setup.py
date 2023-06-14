from setuptools import find_packages, setup


setup(
    name="ctm-python-client",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="2.1.2",
    description="Python Workflows for Control-M",
    long_description="Python Workflows for Control-M",
    author="BMC Software",
    license="BSD 3-Clause",
    keywords="Control-M",
    install_requires=["requests>=2.23.0",
                      "urllib3", "six", "attrs", "certifi", "jinja2"],
    classifiers= [
        "DEVELOPMENT STATUS :: 5 - PRODUCTION/STABLE",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ]
)
