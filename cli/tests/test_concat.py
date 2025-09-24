# Implementing tests for the concat function

import pytest

from click.testing import CliRunner

from pathlib import Path

from cli_tools.fileutils import concat

def test_concat_two_files():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('file1.txt', 'w') as f:
            f.write('File 1 contents.\n')
        with open('file2.txt', 'w') as f:
            f.write('File 2 contents.\n')
        
        result = runner.invoke(concat, ['file1.txt', 'file2.txt', 'combined.txt'])
        assert result.exit_code == 0
        assert Path('combined.txt').exists()

        expected_contents = ['File 1 contents.\n','File 2 contents.\n']
        with open('combined.txt', 'r') as f:
            actual_contents = f.readlines()
        assert actual_contents == expected_contents