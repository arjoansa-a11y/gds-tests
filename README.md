# Lab0 Install Tests

This repository contains a small notebook to validate that the core dependencies for the lab are installed and working. The intended workflow is VS Code on Windows with a WSL (Linux) environment.

## Prerequisites (Windows + WSL)

- Windows 10/11 with WSL 2 enabled.
- A Linux distribution installed via WSL (e.g., Ubuntu 22.04).
- VS Code with the **WSL** extension installed.
- Python 3.10+ available inside WSL.

If you have not configured WSL yet, follow the official Microsoft setup guide and then open VS Code connected to WSL.

## Open the project in WSL

1. Open a WSL terminal.
2. Navigate to the repo folder (or clone it):
   - Clone: `git clone <repo-url>`
   - Then: `cd lab0-install`

VS Code will reopen the folder using the WSL remote environment.

## Create and select a Python environment

From the VS Code WSL window:

1. Ensure **uv** is installed in WSL.
2. Sync the dependencies from `pyproject.toml`:
   - `uv sync`
3. Select the interpreter in VS Code:
   - Command Palette → **Python: Select Interpreter** → choose the `.venv` created by uv (if prompted).

## Install dependencies

Use the repo’s `pyproject.toml` via uv:

```bash
uv sync
```

## Run the notebook

1. Open [install-tests.ipynb](install-tests.ipynb) in VS Code.
2. Ensure the selected kernel uses your `.venv`.
3. Run the cells top-to-bottom.

You should see a waveguide plot in the second cell.

## Troubleshooting

- Email: cccanvas@upv.es