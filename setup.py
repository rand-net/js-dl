import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="js-dl",
    version="0.0.1",
    description="Download javascript libraries  from https://cdnjs.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rand-net/js-dl",
    author="rand-net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["js_dl"],
    include_package_data=True,
    entry_points={"console_scripts": ["js-dl = js_dl.__init__:main"]},
    install_requires=["art", "prompt-toolkit", "requests"],
    keywords=["cdnjs", "javascript", "javascript libraries"],
)
