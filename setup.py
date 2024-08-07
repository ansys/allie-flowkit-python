from setuptools import find_packages, setup

setup(
    name="ansys-allie-flowkit-python",
    version="0.1.0",
    packages=find_packages(include=["app", "docker", "configs"]),
)
