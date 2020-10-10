#!/usr/bin/env python3

from setuptools import setup, find_packages
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

setup(

    name='crackrar',
    install_requires=["rarfile==3.0",
"tqdm",
"more-itertools"
],
   python_requires='>=3',

    # la version du code
    version='1.0',
    packages=find_packages(),
    author="Delevoye Guillaume",
    author_email="delevoye.guillaume@gmail.com",
    description="Projet pour les coding sisters: cracker un fichier rar",
    long_description=open('README.md').read(),
    url='https://github.com/GDelevoye/codingsisters-crackrar',

    include_package_data=True,
    entry_points={'console_scripts': ['crackrar=crackrar.launchers.crackrar:crackrar',"brutegen=crackrar.launchers.brutegen:brutegen"]},

    # La liste des marqueurs autorisés
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.

    classifiers=[
        "Programming Language :: Python",
        "License :: The clear BSD Licence",
        "Natural Language :: French",
        "Operating System :: Ubuntu 18.04 LTS",
        "Programming Language :: Python :: 3.6"
    ],

    license="WTFPL",
)
