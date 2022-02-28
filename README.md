# Mediatree Challenge

https://gitlab.mediatree.fr/-/snippets/67

# how to start the project

create your virtual environment and install dependencies
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

or use then virtual environment already in the project
    source venv/bin/activate

then create database and load the initial datas
    python manage.py migrate
    python manage.py loaddata db.json

now you can start the server
    python manage.py runserver

go to
    http://127.0.0.1:8000/

and log in with username "joe" and password "bar"

# how to start the tests

all test are implemented using Django's tests system, use this command to start all tests

    python manage.py test
