from setuptools import setup,find_packages
from typing import List

REQUIREMENTS_FILE="requirements.txt"
HYPEN_E_DOT="-e ."
def get_requirements()->List[str]:
    """
    This function returns a list of requirements from requirements.txt file
    -> -returns a list of libraries
    """

    with open(REQUIREMENTS_FILE) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements 
setup(
    name='ML project',
    version='0.0.1',
    author='soumya',
    author_email='sowmyah871@gmail.com',
    description='practice project',
    License='MIT License',
    Platform='Visual Studio',
    License_File='LICENSE',
    packages=find_packages(),
    install_requires=get_requirements()
   )