import os
from setuptools import setup


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="GCPUTILS",
    version="0.0.1",
    author="David Istrati",
    author_email="dcistr26@colby.edu",
    description="Util functions for google cloud platform.",
    license="Apache 2",
    keywords="gcp google cloud platform",
    url="",
    install_requires=[
        'oauth2client', 'google-api-python-client', 'tqdm'
    ],
    packages=['src', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2 License",
    ],
)
