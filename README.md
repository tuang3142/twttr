# twttr

## overview

a micro blogging web application that you can run locally

## set up pipenv

clone then cd to this repo on your local machine. the list of required packages can be found in Pipfile and can be ezly installed with `pipenv`, hence setting up `pipenv` is the first thing to do. note that python2 will soon be unsupported so every dependencies are python3 compatible.

```
pip install pipenv
pipenv --three
pipenv shell
pip install
```

## .env file

the app is now only support logging with google. in your own GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET into the environment config. then run `source .env`

## run the app
```
python run.py
```

# api endpoints

`url_prefx = https//localhost/5000`

|      |                  |
|------|------------------|
| GET  | /blogs           |
| POST | /blogs           |
| GET  | /blogs/:id       |
| GET  | /blogs/:id/likes |
| GET  | /users           |
| GET  | /users/:id       |
