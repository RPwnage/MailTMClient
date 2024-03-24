import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setuptools.setup(
    name="MailTMClient",  # This is the name of the package
    version="0.0.3",  # The initial release version
    author="Luca",  # Full name of the author
    description="A Client to easily interact with the MailTM API",
    long_description=long_description,  # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires=">=3.6",  # Minimum version requirement of the package
    py_modules=["MailTMClient"],  # Name of the python package
    package_dir={"": "MailTMClient/"},  # Directory of the source code of the package
    install_requires=[],  # Install other dependencies if any
)
