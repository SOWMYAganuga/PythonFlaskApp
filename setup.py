from setuptools import setup, find_packages

setup(
    name='PythonFlaskApp',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'runapp=app:main',  # Adjust this to your app's entry point
        ],
    },
)
