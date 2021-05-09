import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="fast_deskew",
    version="1.0",
    description="Deskew an image",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Subhamp7/fast_deskew",
    author="Subham Prasad",
    author_email="subham306952@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["fast_deskew"],
    include_package_data=True,
    install_requires=["opencv-python", "scipy"],
    entry_points={
        "console_scripts": [
            "fast_deskew=fast_deskew.__main__:main",
        ]
    },
)