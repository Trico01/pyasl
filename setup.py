from setuptools import setup, find_packages

setup(
    name="pyasl",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "nibabel",
        "scipy",
    ],
    author="Trico",
    author_email="trico010725@gmail.com",
    description="A library for processing ASL MRI data",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/pyasl",
)
