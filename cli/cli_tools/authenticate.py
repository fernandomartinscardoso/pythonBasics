# This file contains the code to authenticate users in a CLI application.

import click

@click.command()
# @click.option('--username', prompt=True)
# # For password, we use `hide_input=True` to not show the password as it's typed
# # and `confirmation_prompt=True` to ask for confirmation of the password:
# @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
# def auth(username, password):
#     """Provides username and password authentication."""
#     click.echo(f'Authenticating {username}...')

# Using other options of prompt to handle username and password input:
def auth():
    """Provides username and password authentication."""
    username = click.prompt('username')
    password = click.prompt('password', hide_input=True, confirmation_prompt=True)
    
    if click.confirm('Are you an admin?'):
        admin_id = click.prompt('Enter your admin ID', type=int, prompt_suffix='>')
        click.echo(f'Logging in admin {username} with ID {admin_id}')
    else:
        click.echo(f'Logging in user {username}')