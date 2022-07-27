# PRICE COMPARISON WEBSITE

## Using postgresql
- download [postgresql](https://www.postgresql.org/download/)
- note: don't install stack builder
-  enter this to the terminal
```bash
createdb -U postgres <db_name>
```
- in settings.py change DATABASES values to :
```python
DATABASES = {
    'default': {
        'ENGINE: 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yourproject',
        'USER': 'yourprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```
- follow [this](https://www.guru99.com/postgresql-create-alter-add-user.html) tutorial to create and add user

## Installing requirements
- enter this to the terminal
```bash
pip install -r requirements.txt
```

### Running the project

1. Clone the repository
2. Create a virtual environment and activate it
```bash
python -m venv [environment name]
```
3. Install the requirements

```bash
 python manage.py runserver 
 ```



## Contributors
[Ydanladi](https://github.com/Ydanladi)
[iEnyene](https://github.com/enyene)
[Ahdeyy](https://github.com/Ahdeyyy)
[fhayvy](https://github.com/fhayvy)
