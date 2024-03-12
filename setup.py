from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="ctm-python-client",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="2.2.3",
    description="Python Workflows for Control-M",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="BMC Software",
    license="BSD 3-Clause",
    keywords="Control-M",
    install_requires=["requests>=2.23.0",
                      "urllib3", "six", "attrs", "certifi", "jinja2"],
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ]
)
