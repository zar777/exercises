from distutils.core import setup

setup(
    # Application name:
    name="clean_project",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Gianluca Parente",
    author_email="gianluca.parente7@gmail.com",

    # Packages
    packages=["project", "project/config"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="",

    #
    # license="LICENSE.txt",
    description="",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
        "psycopg2",
        "pyyaml",
    ],
)
