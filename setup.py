from setuptools import setup, find_packages

setup(
    name="fireprox",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["fire"],
    install_requires=[ "boto3", "tldextract", "tzlocal", "bs4", "lxml" ],
    entry_points={ "console_scripts": [ "fire=fire:main" ] }
)

