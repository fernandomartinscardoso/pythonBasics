# Implementing tests for the authenticate function

import pytest
from click.testing import CliRunner
from cli_tools.authenticate import auth

def test_non_admin_auth():
    runner = CliRunner()
    prompt_inputs = '\n'.join([
        'Adam',        # username
        'password123', # password
        'password123', # confirm password
        'n'            # not an admin
    ])

    result = runner.invoke(auth, input=prompt_inputs)
    assert result.exit_code == 0 # Ensure the command executed successfully, without errors

    expected_output = '\n'.join([
        'username: Adam',
        'password: ',
        'Repeat for confirmation: ',
        'Are you an admin? [y/N]: n',
        'Logging in user Adam',
        ''
    ])

    assert result.output == expected_output

def test_admin_auth():
    runner = CliRunner()
    prompt_inputs = '\n'.join([
        'Adam',        # username
        'password123', # password
        'password123', # confirm password
        'y',            # not an admin
        '42'           # admin ID
    ])

    result = runner.invoke(auth, input=prompt_inputs)
    assert result.exit_code == 0 # Ensure the command executed successfully, without errors

    expected_output = '\n'.join([
        'username: Adam',
        'password: ',
        'Repeat for confirmation: ',
        'Are you an admin? [y/N]: y',
        'Enter your admin ID> 42',
        'Logging in admin Adam with ID 42',
        ''
    ])

    assert result.output == expected_output