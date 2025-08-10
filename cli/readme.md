# Building Python CLI Apps with Click

This repository contains my study material based on the course provided by [Adam McQuistan](https://www.udemy.com/course/building-python-cli-apps-with-click/).

If using VSCode, start virtual environment:

`$ python3 -m venv venv`

`$ source venv/bin/activate`

## Example 1: The Greeter

The command `greetings` is going to invoke __greeter.py__ that prints the greeting on the screen.

After adding your setup file and programming the functions, execute the command to build your editable cli:

`$ pip install -e .`

## Enabling Click

After import Click, you can annotate your command: `@click.command()`
You can also add a documentation message to the command using `"""Message documentation"""` which is going to be accessible via option `--help`.