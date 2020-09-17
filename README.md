# README #

This file will help you to get application up and running.


### Getting Started ###

* Go to PSQL Terminal: "sudo -u postgres psql"
* Create a db for the application: "create database <database_name>;"
* Create user with password: "create user <user_name> with encrypted password < password >;"
* Grant all access to thr user created: "grant all privileges on database <database_name> to <user_name>;"
* Update the above credentials to "youtube_datafetch/environment/local/database.py" file.

### Installing Redis

* Run following commands
1) wget http://download.redis.io/releases/redis-5.0.5.tar.gz
2) tar xzf redis-5.0.5.tar.gz
3) cd redis-5.0.5
4) make
* To Run the server: "src/redis-server"


### Dependency Setup ###

* Make sure you have configured the database.py file correctly.
* Install requirements: "pip install -r requirements.txt".
* Run following command to set environment variable "export DJANGO_SETTINGS_MODULE=youtube_datafetch.settings"
* Run initial django migrations: "python manage.py migrate".
* Create superuser: "python manage.py createsuperuser" for admin interface.
* Enter username, email address, and password 


### For Running Services

* Run Redis Server in one terminal: "redis-server"
* Run Django Server: "python manage.py runserver 0:8000"
* Run RQ Worker: "python manage.py rqworker default"
* Run RQ Scheduler: "python manage.py rqscheduler"
* PS -  Make Sure to run scheduler after the django server and rq worker are initiated.

