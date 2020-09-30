#!/bin/sh
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do    # while port closed
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

#python ./manage.py flush --no-input    # dont work for me
python ./manage.py migrate
python ./manage.py runserver 0.0.0.0:8000

exec "$@"