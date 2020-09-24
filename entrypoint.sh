#!/bin/sh
python ./mysite/manage.py reset_db --noinput
python ./mysite/manage.py migrate
python ./mysite/manage.py add_testing_data
python ./mysite/manage.py runserver 0.0.0.0:8000