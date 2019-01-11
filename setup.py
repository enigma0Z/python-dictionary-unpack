import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="python-dictionary-unpack",
    version="0.0.1",
    description="Dictionary Unpacker",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/enigma0Z/python-dictionary-unpack.git",
    author="Johnathan Bell",
    author_email="enigma.0Z@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
    packages=["Unpack"],
    include_package_data=True,
    install_requires=[""],
    entry_points={}
)
