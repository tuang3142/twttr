# twttr

## overview

a micro blogging web application that you can run locally

## set up pipenv

clone then cd to this repo on your local machine. the list of required packages can be found in Pipfile and can be ezly installed with `pipenv`, hence setting up `pipenv` is the first thing to do. note that python2 will soon be unsupported so every dependencies are python3 compatible.

``` bash
pip3 install pipenv
pipenv --three
pipenv shell
pipenv install
```

## set up mysql database

it is recommended to install both mysql and mysql-sever. below are an example of how to set up mysql database.

``` bash
$ mysql -u root

mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY '14142';

mysql> CREATE DATABASE twttr_db;

mysql> GRANT ALL PRIVILEGES ON twttr_db . * TO 'admin'@'localhost';
```

in your .env file, export the database URI:

``` bash
export SQLALCHEMY_DATABASE_URI=mysql://admin:14142@localhost/twttr_db
```

then run the migration:
``` bash
flask db init
flask db migrate
flask db upgrade
```

## .env file

the app is now only support logging in/out with google. create your own `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` and put it into the environment config then run `source .env`

## run the app

```
python run.py
```

## api endpoints

`prefix = https//localhost/5000/api/v1/`

|methods| endpoint         |
|-------|------------------|
| GET   | /blogs           |
| POST  | /blogs           |
| GET   | /blogs/:id       |
| GET   | /blogs/:id/likes |
| POST  | /blogs/:id/likes |
| GET   | /users           |
| GET   | /users/:id       |
| GET   | /google/login    |
| POST  | /google/login    |
| GET   | /google/logout   |
