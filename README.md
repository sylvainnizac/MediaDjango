# Mediatree Challenge

https://gitlab.mediatree.fr/-/snippets/67

# for translations
gettext 0.15+

# how to start the project

python manage.py migrate
python manage.py loaddata db.json

# how to start the tests

all test are implemented using Django's tests system, use this command to start all tests

python manage.py test