from setuptools import setup

setup(
    name='cli_tools',
    version='0.1',
    py_modules=['greeter'],
    install_requires=[
        'Click'
    ],
    entry_points={
        'console_scripts': 'greetings=greeter:greet',
    }
)