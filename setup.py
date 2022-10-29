
from setuptools import setup, find_packages

with open("Readme.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="processamento_de_imagens",
    version="0.0.1",
    author="Laury",
    author_email="lauryzinha@gmail.com",
    description="Projeto para aula DIO (Pior aula que eu já assisti)",
    packages=find_packages(),   
    pyhhon_requires='>=3.5',
)