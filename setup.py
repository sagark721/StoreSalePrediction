from typing import List
from matplotlib.artist import get
from setuptools import setup,find_packages

PROJECT_NAME = "Store_Sale_Prediction"
VERSION ="1.0.0"
AUTHOR = " Sagar. S. Kanade"
AUTHOR_EMAIL_ID = "sagarkanade2121@gmail.com"
REQUIREMENTS_FILE = "requirements.txt"


def get_package_details() -> List[str]:
    with open(REQUIREMENTS_FILE,'r') as requirements:
        return requirements.readlines().remove("-e .")





setup(
    name=PROJECT_NAME,
    version=VERSION,
    description= "Store Sales Prediction Project",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL_ID,
    packages=find_packages(),
    install_requires = get_package_details()

)