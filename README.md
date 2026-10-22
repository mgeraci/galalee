# Galalee

A simple Django app for a musician's website. https://galalee.com

## Installation

1. Clone the repo and cd into it.
1. Create a python virtual environment (python 3): `python -m venv galalee-venv`.
1. Activate the virtual environment: `source galalee-venv/bin/activate`.
1. Install the python packages: `pip install -r requirements.txt`
1. Create a local MySQL database (note the name and user/password for the next step)
1. Create a `localsettings.py` file (which will be git ignored) to the `galalee` folder (example contents below)
1. Set up the database tables: `./manage.py migrate`
1. If not importing existing data: `./manage.py createsuperuser` (you can use this to log in at localhost:8000/admin)
1. Start the server: `./manage.py runserver`

Then you can visit localhost:8000 and you should see the site. Admin panel login is at localhost:8000/admin.

To run the app after installation:

1. `source galalee-venv/bin/activate`
1. `./manage.py runserver`

## Local Settings

`localsettings.py`

```.py
DEBUG = True
SECRET_KEY = '[your secret key]'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '[database name]',
        'USER': '[username]',
        'PASSWORD': '[password]'
    }
}
```
