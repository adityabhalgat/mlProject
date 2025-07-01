from setuptools import find_packages , setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
   
    """
    This function will return the list of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(    
    name='MlProject',
    version='2025.1.1',
    author='Aditya Bhalgat',
    author_email='adityabhalgat81@gmail.com',
    packages = find_packages(),
    description='A Machine Learning Project Template',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=get_requirements('requirements.txt'),
    )

