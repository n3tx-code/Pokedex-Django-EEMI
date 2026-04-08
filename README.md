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
pip install -r requirements.txt
```

4. Run the development server

```bash
python manage.py runserver
```

# Migration

1. Make migrations

```bash
python manage.py makemigrations
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

2. Import the models

```python
from .models import Pokemon
```

3. Create a pokemon in the shell

```python
Pokemon.objects.create(name="Pikachu")
```
