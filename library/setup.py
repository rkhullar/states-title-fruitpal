import pipfile
from setuptools import find_packages, setup

from fruitpal import __version__


def load_requirements() -> list[str]:
    return [f'{package}{version}' for package, version in pipfile.load().data['default'].items()]


def read_python_version() -> str:
    return pipfile.load().data['_meta']['requires']['python_version']


setup(
    name='fruitpal',
    version=__version__,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires='~='+read_python_version(),
    install_requires=load_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Private :: Do not Upload'  # prevents accidental uploading
    ],
    entry_points={
        'console_scripts': [
            'fruitpal=fruitpal.command_line:main'
        ]
    }
)
