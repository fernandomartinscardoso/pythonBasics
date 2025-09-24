# This program calculates the sum and difference of numbers provided as command-line arguments.

import click

@click.command()
@click.argument('xs', type=int, nargs=-1)
@click.option('-v', '--verbose',
              help='Shows additional output',
              count=True) # is_flag allows the option to be a boolean flag, so it can be used without a value
def add(xs, verbose):
    """This command adds numbers."""
    if verbose > 1:
        steps = [xs[0]]
        for x in xs[1:]:
            steps.append(x)
            click.echo(f"{' + '.join(str(s) for s in steps)} = {sum(steps)}")
    elif verbose == 1:
        click.echo(f"{' + '.join(str(x) for x in xs)} = {sum(xs)}")
    else:
        click.echo(sum(xs))

@click.command()
@click.argument('xs', type=int, nargs=-1)
@click.option('-v', '--verbose',
              help='Shows additional output.',
              is_flag=True) # is_flag allows the option to be a boolean flag, so it can be used without a value
def subtract(xs, verbose):
    """This command subtracts numbers."""
    result = xs[0]
    for x in xs[1:]:
        result -= x
    
    if verbose:
        click.echo(f"{' - '.join(str(x) for x in xs)} = {result}")
    else:
        click.echo(result)
