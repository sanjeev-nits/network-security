from setuptools import setup,find_packages
from typing import List


def get_requirements() -> List[str]:
    requirements_lst:list[str] = []
    try:    
        with open('requirements.txt', 'r') as f:
            lines=f.readlines()

            for line in lines:
                requirements=line.strip()

                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)

    except FileNotFoundError:
        print("File not found.")

    return requirements_lst

setup(
    name='network_security',
    version='0.0.1',
    packages=find_packages(),
    author='Sanjeev Kumar',
    author_email='sanjeevkumar814155@gmail.com',
    description='A network security project',
    install_requires=get_requirements()
)
   

