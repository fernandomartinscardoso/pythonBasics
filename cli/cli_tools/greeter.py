# This program gives a greeting message to the user.

import click

@click.command()
def greet():
    # Documentation for the greet command, accessible via --help
    """Displays a greeting message to the user."""
    # print("Hello! Welcome to our program.")
    # As a best practice, we should use click's echo function
    click.echo("Hello! Welcome to our program.")
