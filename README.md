# README

## installation

1. clone the repo, delete .git, create a new git repo
2. setup name & description in `pyproject.toml`
3. `poetry install`
4. rename and config your `project.code-workspace` settings
5. happy-coding

## notebooks

to work with notebooks, set
DJANGO_ALLOW_ASYNC_UNSAFE=true in your .env

## production

fix the settings in settings.py, don't use the `.env`

## for docker, postgreSQL, redis & celery see the more advanced skeleton
