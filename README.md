test Django project

To start app:

Creare .env files which will be used to configure the connection to the database  (you can find samle in .env.samlpe)

docker-compose -f docker-compose.prod.yml up -d --build

use 

http://localhost:1337/polls/

or 

http://localhost:1337/admin/

to see the application

or

http://localhost:1337

to upload your file 