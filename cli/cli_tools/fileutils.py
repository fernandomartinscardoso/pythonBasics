# This section of the code is for manipulation of file arguments using Click.

import typing # Ensure typing is imported for more advanced type modes
import click
import requests

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

@click.command()
@click.argument('inputs', nargs=-1) # Accept multiple input file paths
def download(inputs):
    """Downloads files from given (url, filename) input pairs and saves them locally.

    Example: 
    
        download <url1>,<filename1.txt> <url2>,<filename2.txt> ...
    """
    with click.progressbar(
        length=len(inputs), # Total number of items to process
        show_eta=False, # Disable ETA (Estimated Time of Arrival) display for simplicity
        item_show_func=lambda fname: f"Downloading {fname}" # Custom function to show the current item being processed
    ) as bar:
        for i, item in enumerate(inputs, start=1): # Starting index at 1 to avoid zero-based indexing in display, i.e., message showing "Downloading None"
            url, filename = item.split(',') # Split each input into URL and filename based on comma
            response = requests.get(url)
            with open(filename, 'w') as fo:
                fo.write(response.text)
            bar.update(i, filename) # Update the progress bar with the current filename
    
    click.echo("All downloads completed.")
