# how to start the project

create your virtual environment

    python -m venv venv
    source venv/bin/activate

install backend dependencies through pip

    pip install -r requirements.txt

and install frontend dependencies through npm

    npm install --no-save

then create database and load the initial datas

    python manage.py migrate
    python manage.py loaddata db.json

create user

    python manage.py createsuperuser --username=username --email=email@example.com

now you can start the server

    python manage.py runserver

go to http://127.0.0.1:8000/

and log in with your username and password

# how to start the tests

all test are implemented using Django's tests system, use this command to start all tests

    python manage.py test
