# python setup.py develop
from setuptools import setup

# beschreibt notwendige Informationen auf pypi
# PyVersionen können durch :: getrennt werden: geht auch:
# Programming Language :: Python :: 3.7 :: or higher
CLASSIFIERS = '''\
License :: OSI Approved
Programming Language :: Python :: 3.7 :: 3.8
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
'''
# Distname hat gleichen Namen wie Ordnername
# grundlegende Versionen
DISTNAME = 'fastvector'
AUTHOR = 'Jan Schaffranek'
AUTHOR_EMAIL = 'jan.schaffranek@email.com'
DESCRIPTION = 'This is a simple vector python package.'
LICENSE = 'MIT'
# Beschreibung on pypi
README = 'This is a simple vector python package.'

# Release Information
VERSION = '0.1.0'
ISRELEASED = False

# Python Versionen und Module und lokale Packages
PYTHON_MIN_VERSION = '3.7'
PYTHON_MAX_VERSION = '3.8'
PYTHON_REQUIRES = f'>={PYTHON_MIN_VERSION}, <={PYTHON_MAX_VERSION}'

INSTALL_REQUIRES = [
    'numpy',
    'scipy',
    'Cython'
]

# required
PACKAGES = [
    'fastvector',
    'tests'
]


# Alle Informationen werden in einem Dictionary abgespeichert
metadata = dict(
    # required
    name=DISTNAME,
    # required
    version=VERSION,
    long_description=README,
    packages=PACKAGES,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    # wichtig: CLASSIFIERS ist eine liste
    classifiers=[CLASSIFIERS],
    license=LICENSE
)


def setup_package() -> None:
    setup(**metadata)


if __name__ == '__main__':
    setup_package()
