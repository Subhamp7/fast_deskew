
from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0'
DESCRIPTION = 'Deskew any images faster than ever'
HERE = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(HERE, "README.md"), encoding="utf-8") as file_read:
    long_description = "\n" + file_read.read()

# Setting up
setup(
    name="fast_deskew",
    version=VERSION,
    author="Subham Prasad",
    author_email="subham306952@gmail.com",
    url="https://github.com/Subhamp7/fast_deskew",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="MIT",
    packages=find_packages(),
    #install_requires=['opencv-python>=3', 'numpy', 'scipy'],
    python_requires='>=3',
    keywords=['python','deskew','open cv', 'skew'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers"
    ]
)

