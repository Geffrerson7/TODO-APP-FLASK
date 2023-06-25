# TODO-APP-FLASK

## Description

App made with Flask and Python to create tasks, mark tasks as done and edit tasks.

## Getting Started

First clone the repository from Github and switch to the new directory:
```bash
  $ clone git https://github.com/Geffrerson7/TODO-APP-FLASK.git
```

```bash
  $ cd TODO-APP-FLASK
```

Activate the virtualenv for your project.

```sh
$ virtualenv venv
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Install project dependencies:
```sh
(env)$ pip install -r requirements.txt
```

Create the following environment variables in the .env file

`FLASK_APP`

`FLASK_DEBUG`

`FLASK_ENV`

`SECRET_KEY`

`DATABASE_URI`

`DB_NAME`

You can now run the development server:
```sh
(env)$ flask run
```

And navigate to
```sh
http://127.0.0.1:5000/
```

## Project installation in Docker

Clone the repository

```bash
$ git clone https://github.com/Geffrerson7/TODO-APP-FLASK.git
```

Go to the project directory.

```bash
$ cd TODO-APP-FLASK
```

Run the command
```sh
$ docker-compose up
```

And navigate to the route
```sh
http://127.0.0.1:8000/
```

## Author

- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
