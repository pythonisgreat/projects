try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'ex47',
    'author': 'Nick',
    'url': 'firstproject',
    'download_url': 'downloadfirstproject',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'hello_world'
}

setup(**config)
