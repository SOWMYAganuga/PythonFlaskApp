from setuptools import setup, find_packages

setup(
    name='PythonFlaskApp',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        # Add other dependencies from your requirements.txt here
    ],
)
