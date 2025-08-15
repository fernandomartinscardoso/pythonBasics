# This program gives a greeting message to the user.

import click

@click.command()
@click.argument('first_name')
@click.argument('last_name')
# @click.option('-l','--lang', 
#               help='Specify the language for the greeting: English (en) or Spanish (es)', 
#               default='en')
# def greet(first_name, last_name, lang):
#     # Documentation for the greet command, accessible via --help
#     """Displays a greeting message to the user."""
#     # print("Hello! Welcome to our program.")
#     # As a best practice, we should use click's echo function instead of print
#     if lang == 'es':
#         click.echo(f"¡Hola, {first_name} {last_name}! Bienvenido a nuestro programa.")
#     elif lang == 'en':
#         click.echo(f"Hello, {first_name} {last_name}! Welcome to our program.")
#     else:
#         raise click.BadOptionUsage('lang', 
#                                    f"Unsupported language '{lang}'. Please use 'en' for English or 'es' for Spanish.")
    
# Adding type=click.Choice to the lang option simplifies the validation of the input:
@click.option('-l','--lang', 
              help='Specify the language for the greeting: English (en) or Spanish (es)', 
              default='en',
              type=click.Choice(['en', 'es']))
@click.option('--say-it',
              type=int,
              default=1,
              help='Number of times to repeat the greeting')
def greet(first_name, last_name, lang, say_it): # Click expects the dashes in the option names to be replaced with underscores in the function parameters.
    # Documentation for the greet command, accessible via --help
    """Displays a greeting message to the user."""
    greetings = f"Hello, {first_name} {last_name}! Welcome to our program." if lang == 'en' else f"¡Hola, {first_name} {last_name}! Bienvenido a nuestro programa."
    for _ in range(say_it):
        # Using click's echo function instead of print for better compatibility with Click's command line interface
        click.echo(greetings)
    