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

In __calculator.py__ is described the option to add verbose in your CLI. The [original McQuistan file for stack verbosity](https://github.com/fernandomartinscardoso/pythonBasics/blob/main/cli/originalMcQuistanFiles/07-options-ints-and-bools.zip) contains an extra implementation for stack verbose display.

## Example 3: The Authenticator

The command `authenticate` invoked by __authenticate.py__ alows to add users and passwords. For password, we use `hide_input=True` to not show the password as it's typed and `confirmation_prompt=True` to ask for confirmation of the password.

In the class [Prompt Types and User Confirmation](https://github.com/fernandomartinscardoso/pythonBasics/blob/main/cli/originalMcQuistanFiles/10-prompt-ints-and-confirm.zip) McQuistan teach how to use integer as ID to create special confirmation access (for an admin account, for instance).

## Example 4: Files Manipulation

The commands invoked by __fileutils.py__ allow some basic file manipulations. The command `note` writes notes input to a given file, and the command `concat` concatenates the contents of one or more files into a single output file. The file __combined.txt__, for instance, was created with command `concat file1.txt file2.txt file3.txt combined.txt`.

In the application __notes.py__, it is shown how to create nested commands using `@click.group()` class. This code provides a simple CLI to create, delete, add, and update notes to a database, showing the contents, date, and time of modification. The code was also adapt to contain shared context of grouped commands, which simplifies the implementation using object-oriented approach.

## Example 5: Progress Bar

The command `download` invoked by __fileutils.py__ allows to download text files from URLs, and it contains the standard Click progress bar, which is quite useful to check if the download is finished or how much of it is done.

By using the option `click.progressbar(inputs)` directly, the progress bar is only checking iterably how many items were downloaded. By expanding the arguments, you can give more functionalities and see more details on the progress. For example:

`click.progressbar(
        length=len(inputs),
        show_eta=False,
        item_show_func=lambda fname: f"Downloading {fname}"
    )`

where `length=len(inputs)` specifies the total nuimber of items to process, `show_eta=False` disables the estimated time of arrival, and `item_show_func=lambda fname: f"Downloading {fname}"` shows the current item being processed.

## Style

Using the command `click.style(<message>,options)`, the messages on the prompt can be modified in terms of foreground and background colors, typefaces, and many more, as per [Click Documentation](https://click.palletsprojects.com/en/stable/).

Since this command is commonly grouped with `click.echo()` to show messages, there is also the command `click.secho()` to combine both functionalities. Therefore, e.g, `click.echo(click.style(greetings, fg='green', bold=True, bg='yellow'))` and `click.secho(greetings, fg='green', bold=True, bg='yellow')` are equivalents.
