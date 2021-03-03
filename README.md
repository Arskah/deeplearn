# Deeplearn local setup with Poetry

## Prerequisities

- Python 3.X (`pyproject.toml` assumes ^3.9, but could be an older version)
- Poetry [https://python-poetry.org/docs/](https://python-poetry.org/docs/)

## Installation

- Recommendation: install virtualenv inside project folder (`.venv` folder, so VSCode can recognise python executable) with

  ```bash
  poetry config virtualenvs.in-project true
  ```

- Install dependencies

  ```bash
  poetry install
  ```

## Running

- Start shell within venv with

  ```bash
  poetry shell
  ```

- Start notebook with

  ```bash
  jupyter notebook
  ```
