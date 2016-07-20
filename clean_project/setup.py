from distutils.core import setup

setup(
    name="clean_project",

    version="0.1.0",

    author="Gianluca Parente",
    author_email="gianluca.parente7@gmail.com",

    packages=["project", "project/config"],

    include_package_data=True,

    url="",

    license="LICENSE.txt",

    description="Useful project in which is possible to remove all punctuation in a bunch of files,"
                " indexing and inserting them in a database table. At the end of this phases,"
                " it's possible to do a search of a word(in the table) to know in which files and lines numbers is it",

    install_requires=[
        "flask",
        "psycopg2",
        "pyyaml",
    ],
)
