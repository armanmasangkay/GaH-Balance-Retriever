from setuptools import setup
setup(
    name = 'gah balance retriever',
    version = '0.1.0',
    packages = ['gah'],
    entry_points = {
        'console_scripts': [
            'gah = gah.__main__:main'
        ]
    })