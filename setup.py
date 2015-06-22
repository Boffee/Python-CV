try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Computer Vision',
    'author': 'Zhenbang Li',
    'packages': [],
    'requires': ['NumPy', 'Matplotlib', 'SciPy', 'PIL']
}

setup(**config)