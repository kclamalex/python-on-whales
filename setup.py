from setuptools import find_packages, setup

setup(
    name="docker-cli-wrapper",
    version=0.1,
    install_requires=["typeguard"],
    packages=find_packages(),
)