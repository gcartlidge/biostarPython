from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='biostarPython',
    version='0.3.0.2',
    author_email = 'gcartlidge@supremainc.com',
    author = 'SupremaUK',
    description = 'Python client for Suprema GSDK with included callable classes.',
    long_description=README,
    long_description_content_type="text/markdown",
    url = 'https://github.com/gcartlidge/biostarPython',
    packages=['biostarPython','biostarPython.service','biostarPython.proto'],
    python_requires='>3.5.2',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    package_data={
        "": ["*.py", "*.proto", "*.json"],
        "proto": ["*.proto"],
        "service": ["*.py"],
    },
    install_requires=[
        'grpcio',
        'protobuf',
    ],
)