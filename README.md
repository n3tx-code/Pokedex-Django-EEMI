# Installation

1. Create virtual environment

```bash
python3 -m venv env
```

2. Activate virtual environment

```bash
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. Install dependencies

```bash
pip install Django
```

4. Create Django project

```bash
django-admin startproject Pokedex_EEMI .
```

5. Run the development server

```bash
python manage.py runserver
```

6. To create a new app called "pokemon"

```bash
./manage.py startapp pokemon
```

# Migration

1. Make migrations for the "pokemon" app

```bash
python manage.py makemigrations pokemon
```

2. Apply the migrations to the database

```bash
python manage.py migrate
```

# Django shell

1. Open the Django shell

```bash
python manage.py shell
```

2. Create a pokemon in the shell

```python
from pokemon.models import Pokemon

Pokemon.objects.create(name="Pikachu")
```
