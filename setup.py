from setuptools import find_packages, setup


def read_requirements(file_path):
    with open(file_path) as f:
        return f.read().splitlines()



setup(

name = 'sensor_fault_detection',
version="0.0.1",
author="sam",
packages=find_packages(),
install_requires=read_requirements("requirements.txt")
)