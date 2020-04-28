# README

## installation

1. clone the repo, delete .git, create a new git repo
2. setup name & description in `pyproject.toml`
3. `poetry install`
4. `poetry shell` to activate your env
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py runserver` exposes the server on localhost:8000
8. happy-coding

## notebooks

to work with notebooks, set
`DJANGO_ALLOW_ASYNC_UNSAFE=true` in your `.env`

## production

fix the settings in settings.py, don't use the `.env`

## other skeletons

[minimal django sqlite](https://github.com/oryon-dominik/skeleton-django-sqlite-minimal) (this repo)
[minimal django with a small CRUD example](https://github.com/oryon-dominik/skeleton-django-sqlite-crud)
[django with postgres & docker](https://github.com/oryon-dominik/skeleton-django-postgres-docker)
[minimal django integrated with vue & parceljs](https://github.com/oryon-dominik/skeleton-django-vue-parceljs)
