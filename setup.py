from setuptools import setup, find_packages

setup(
    name='InsightX',
    version='0.1.0',
    packages=find_packages(include=['InsightX', 'tests']),
    install_requires=[
        'requests',
        'matplotlib',
        'python-dateutil'
    ],
    entry_points={
        'console_scripts': [
            'InsightX = tests.test_api:main',  # If you want a command-line interface
        ],
    },
)