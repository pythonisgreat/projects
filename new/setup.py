try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'Delete Restricted File',
    'author': 'Nick',
    'url': 'deleteitem',
    'download_url': 'download-deleteitem',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['delete'],
    'scripts': [],
    'name': 'delete_item'
}

setup(**config)
