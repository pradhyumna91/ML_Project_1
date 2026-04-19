
from setuptools import setup, find_packages
from typing import List

def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace('\n','') for req in requirement]

        if -e in requirement:
            requirement.remove('-e .')
            
    return requirement




setup(
    name='my_package',
    version='0.1.0',
    author='Pradhyumna Kiledar',
    author_email='pradhyumnakiledar91@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')
)