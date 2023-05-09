#!/bin/bash
source env/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py createsu
python manage.py runserver