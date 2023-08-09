

from setuptools import setup
import os
import pkg_resources

setup(
    name="Sort Files",
    version="0.1",
    description='Script para organizar archivos',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    author="Leo",
    url="https://github.com/CalumRakk/sort_files",
    install_requires=["filetype==1.2.0"],
    entry_points={
        "console_scripts": ["sort_files=sort_files.cli:run_script"],
    },
    packages=['sort_files'],
)