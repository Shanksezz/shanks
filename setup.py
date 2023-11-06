from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess
import sys

# Custom installation class to run 'b2' commands
class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        self.run_command("run_b2_release")

# Custom development installation class
class CustomDevelopCommand(develop):
    def run(self):
        develop.run(self)
        self.run_command("run_b2_release")

# Custom command to run 'b2' release commands
from distutils.cmd import Command
class RunB2Release(Command):
    description = "Run 'b2' release commands"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # Replace 'b2' with your actual command
        commands = [
            "b2 release python=3.7 stage_module stage_dependencies",
            "b2 release python=3.7 install_module",
            # Add other 'b2' commands here if needed
        ]

        for command in commands:
            subprocess.run(command, shell=True, check=True)

setup(
    name='your_package_name',
    version='1.0',
    packages=find_packages(),
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        'run_b2_release': RunB2Release,
    },
    install_requires=[
        # Specify your dependencies here
        'libtorrent',  # Assuming you have libtorrent as a dependency
    ],
    # Other package information
    author='Your Name',
    author_email='your@email.com',
    description='Your package description',
)
