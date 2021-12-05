from setuptools import setup, find_packages

with open('requirements.txt', "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dotory_fairy_tale_image_style_transfer",
    version="0.0.1",
    author="DOTORY",
    author_email="developer@dotoryspace.com",
    description="dotory fairy tale image style transfer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dotory-space/dotory_fairy_tale_image_style_transfer.git",
    packages=find_packages(),
    install_requires=requirements,
)
