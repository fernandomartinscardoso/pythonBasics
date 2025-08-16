# This section of the code is for manipulation of file arguments using Click.

import typing # Ensure typing is imported for more advanced type modes
import click

@click.command()
@click.argument('fo', type=click.File('a')) # 'a' mode for appending
def note(fo: typing.IO):
    """Write notes input to a given file."""
    click.echo('Enter lines of text below and press Ctrl+C to save and exit.')
    try:
        while True:
            value = click.prompt('', prompt_suffix='>') # Prompt for input. Provides a suffix for clarity.
            fo.write(f'{value}\n')
    except click.Abort:
        click.echo(f'\nNotes saved to {fo.name}.')
