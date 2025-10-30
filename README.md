# 📚 Python Algorithms and Data Structures Study Repository

[![Static Badge](https://img.shields.io/badge/3.x-6771B0?logo=python&logoColor=white&label=Python)](https://www.python.org/)
[![GitHub License](https://img.shields.io/github/license/fernandomartinscardoso/pythonBasics?color=67B082)](https://github.com/fernandomartinscardoso/pythonBasics/blob/main/LICENSE)

This repository serves as a personal learning and practice sandbox for fundamental algorithms and data structures, implemented in Python. It also hosts various small-scale test projects designed to reinforce programming concepts and explore different modules.

## 🎯 Purpose

The primary goals of this repository are:

- Deepen understanding of core algorithmic concepts (e.g., sorting, searching, graph traversal) and their efficient Python implementations.

- Practice implementing common data structures (e.g., linked lists, stacks, queues, trees) from scratch.

- Maintain a clean, executable codebase of solutions to classic computer science problems.

- Provide a testing ground for small, self-contained Python projects and utility scripts.

## 📂 Repository Structure

To be added.

## 🚀 Getting Started

To explore or run the code in this repository, follow these steps:

1. Ensure Python is installed: This repository is developed using Python 3.13 or higher.
2. Install dependencies (if any): While most algorithm files are pure Python, some test projects may require external libraries.
   To be completed: list of [requirements](https://github.com/fernandomartinscardoso/pythonBasics/blob/main/requirements.txt) to be installed.

   ```bash
   pip install -r requirements.txt
   ```

3. Run tests (recommended): Navigate to the `tests/` directory and execute the test suite to verify implementations. For now, only `cli/` repository has test suite implemented, but others will be added as the study evolves.

## 💻 Virtual environment in VS Code

### 1. Create the Virtual Environment

Use the built-in Python module, `venv`, to create the environment. Open your integrated terminal in VS Code (usually Ctrl + ` or View -> Terminal) and run the appropriate command based on your system.

Navigate to your project's root directory first.

- __For Windows__ (Command Prompt or PowerShell)
  Use the `venv` module:

  ```bash
  python -m venv .venv
  ```

- __For macOS/Linux__ (Bash/Zsh)
  Use the `python3` command (or just `python` if that points to your desired version):

  ```bash
  python3 -m venv .venv
  ```

- `.venv`: This is the conventional name for the environment directory. You can choose any name, but `.venv` is widely recognized and often automatically ignored by Git.

### 2. Activate the Virtual Environment

Activating the environment ensures that any packages you install with `pip` go into this isolated environment instead of your global Python installation.

- __For Windows__ (Command Prompt)

  ```bash
  .venv\Scripts\activate.bat
  ```

- __For Windows__ (PowerShell)

  ```bash
  .venv\Scripts\Activate.ps1
  ```

  _(Note: If PowerShell prevents execution due to execution policy, you might need to temporarily run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`.)_

- __For macOS/Linux__ (Bash/Zsh)

  ```bash
  source .venv/bin/activate
  ```

- __Verification__
  Once activated, your terminal prompt should change to show the environment's name in parentheses, like `(.venv) your_username@computer:~/project_folder$`.

### 3. Configure VS Code to Use the Environment

While VS Code is often smart enough to detect a newly created `.venv` folder, you should explicitly select the interpreter to ensure it uses the correct environment for running, debugging, and IntelliSense.

1. Open the Command Palette in VS Code (__Ctrl + Shift + P__ or __Cmd + Shift + P__).

2. Type: `Python: Select Interpreter`

3. Choose the command when it appears.

4. VS Code will present a list of detected interpreters. Select the one pointing to your newly created environment, usually listed as `./.venv/bin/python` (or `.venv\Scripts\python.exe` on Windows).

After selection, the interpreter path will appear in the bottom-right corner of the VS Code window, confirming that VS Code is now using the isolated environment for your project. You can now install your dependencies from your `requirements.txt` (Step 2 of __Getting Started__ section).

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/fernandomartinscardoso/pythonBasics/blob/main/LICENSE) file for details.
