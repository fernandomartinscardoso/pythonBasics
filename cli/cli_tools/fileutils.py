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

@click.command()
@click.argument('inputs', type=click.File('r'), nargs=-1) # Accept multiple input files in read mode, nargs=-1 allows for multiple files
@click.argument('output', type=click.File('w')) # Single output file in write mode
def concat(inputs: typing.Collection[typing.IO], output: typing.IO):
    """Concatenates the contents of one or multiple input files into a single output file."""
    for fi in inputs:
        for line in fi:
            output.write(line)
        click.echo(f'{fi.name} written to {output.name}.')
