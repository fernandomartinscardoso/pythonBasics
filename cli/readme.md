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

## Example 2: The Calculator

The commands invoked by __calculator.py__ are going to support the knowledge on arguments.

To add arguments, you may follow with the annotation __argument__: `@click.argument(<var_name>)`. You can add as many arguments as you need, they are going to be read from top to bottom.

The default type of argument is __string__. But you can use the option `type` inside the argument to define a different type. Generic example `@click.argument(<var_name>, type=<typ_name>)`, where `<typ_name>` can be `int`, `float`, etc.

After adding new functions, you may execute the installation command `$ pip install -e .` to make the new functions available.

Click supports variable number of arguments to a function (_variadic_), since this resource is also available for [Python language](https://www.geeksforgeeks.org/python/args-kwargs-python/). Generic example: `@click.argument(<var_name>, type=<typ_name>, nargs=-1)`.

## Options

Let's improve the greeter with option of multiple languages to check how __options__ work in Click.

You can add options to you CLI by using the annotation `@click.option('--<opt-name>', help='Help text')`.

Click expects the dashes in the option names to be replaced with underscores in the function parameters. So, `<opt-name>` at `click.option` would become ``<opt_name>` in the function parameters.

In __calculator.py__ is described the option to add verbose in your CLI. In case you want to add stack verbosity, the McQuistan original files contain this implementation [here](/originalMcQuistanFiles/07-options-ints-and-bools.zip).

## Example 3: The Authenticator

The command `authenticate` invoked by __authenticate.py__ alows to add users and passwords. For password, we use `hide_input=True` to not show the password as it's typed and `confirmation_prompt=True` to ask for confirmation of the password.
