Display a preview of media files in the Django admin

### Poetry
This project uses [Poetry](https://python-poetry.org/docs/) for dependency management and packaging.

Install Poetry and add Poetry to [Path](https://python-poetry.org/docs/#installation).

**Debian / Ubuntu / Mac**

`curl -sSL https://install.python-poetry.org | python3 -`

**Windows**

open powershell and run: `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

## Development

### Dev Setup

Setup basic `.env` for development: `cp .env.template .env`

Install dependencies: `poetry install`

Install the defined pre-commit hooks: `poetry run pre-commit install`

Activate the virtualenv: `poetry shell`

Run the Django dev server: `./manage.py runserver` or `python manage.py runserver`