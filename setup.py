import re

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

from devx import __version__

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    long_description = re.sub(r"\n!\[.*\]\(.*\)", "", long_description)
    long_description = re.sub(r"\n- \[.*\]\(#.*\)", "", long_description)

setup(
    name="evolve-devx",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "devx = devx.main:main",
        ],
    },
    description="devx is GPT powered coding in your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evolve-community/devx",
)
