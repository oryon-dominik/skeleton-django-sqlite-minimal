# README

## installation

1. use this repo as a template, clone the repo
2. setup name & description in `pyproject.toml`
3. create a dotenv `touch .env` where the projects environment variables will get set to. (you may use the example `cp .env.example .env`)
4. `poetry install`
5. activate the venv just created with `poetry shell` or `workon <venv-name>` (I recommend using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/))

Now comes the django-part

6. Create migrations for your models `python manage.py makemigrations` (repeat this anytime you change your models)
7. Apply the migrations to the database `python manage.py migrate`
8. If you need an adminuser also create it with `python manage.py createsuperuser`
9. `python manage.py runserver` exposes the server on localhost:8000

Happy-coding =)

## notebooks

We can use notebooks for an easy access to in interactive django-shell. (To debug, develop or create model-instances on the fly)
To work with notebooks, set `DJANGO_ALLOW_ASYNC_UNSAFE=true` in your `.env` an run:

    python manage.py shell_plus --notebook

## production

fix the settings in settings.py, (remember `DEBUG=false` in production!)

## other skeletons

[minimal django sqlite](https://github.com/oryon-dominik/skeleton-django-sqlite-minimal) (this repo)
[minimal django with a small CRUD example](https://github.com/oryon-dominik/skeleton-django-sqlite-crud)
[django with postgres & docker](https://github.com/oryon-dominik/skeleton-django-postgres-docker)
[minimal django integrated with vue & parceljs](https://github.com/oryon-dominik/skeleton-django-vue-parceljs)
