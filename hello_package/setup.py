from setuptools import setup
setup(
    name = 'helloworld',
    version = '0.0.1',
    description = 'Say Hello',
    py_modules = ['helloworld'],
    package_dir = {'': 'src'},
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Lnaguage :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
)