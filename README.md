# README

## installation

The repository setup

1. Use this [repo as a template](https://github.com/oryon-dominik/skeleton-django-sqlite-minimal/generate) for your own, then clone it `git clone <repository-address> <target>`.
2. Setup name & description in `pyproject.toml`.
3. Create a dotenv `touch .env` where the projects environment variables will get set to. (you may use the example `cp .env.example .env`).
4. For dependency-management I use [poetry](https://python-poetry.org/). If poetry is installed, install the dependencies with `poetry install`.
5. Activate the venv just created with `poetry shell` or `workon <venv-name>` (I recommend using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)).

The django-part

6. Create migrations for your models `python manage.py makemigrations` (repeat this anytime you change your models).
7. Apply the migrations to the database `python manage.py migrate`.
8. If you need an adminuser also create it with `python manage.py createsuperuser`.
9. `python manage.py runserver` exposes the server on localhost:8000.

Happy coding =)

## notebooks

We can use notebooks for an easy access to an interactive django-shell. (To debug, develop or create model-instances on the fly)  
To work with notebooks, set `DJANGO_ALLOW_ASYNC_UNSAFE=true` in your `.env` an run:

    python manage.py shell_plus --notebook

## production

Fix the settings in settings.py, (remember to set `DEBUG=false` in production!)

## other skeletons

[minimal django sqlite](https://github.com/oryon-dominik/skeleton-django-sqlite-minimal) (this repo)  
[minimal django with a small CRUD example](https://github.com/oryon-dominik/skeleton-django-sqlite-crud)  
[django with postgres & docker](https://github.com/oryon-dominik/skeleton-django-postgres-docker)  
[minimal django integrated with vue & parceljs](https://github.com/oryon-dominik/skeleton-django-vue-parceljs)  
