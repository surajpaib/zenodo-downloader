from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zenodo-downloader",
    version="0.1.0",
    author="Suraj",
    description="A command-line tool to download files from Zenodo records",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/surajpaib/zenodo-downloader",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "tqdm>=4.50.0",
    ],
    entry_points={
        "console_scripts": [
            "zenodo-download=zenodo_downloader.cli:main",
        ],
    },
)
