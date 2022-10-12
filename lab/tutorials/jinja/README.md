# CKAN 101 - Lab - Jinja tutorial

A simple web app built on top of [Flask](https://flask.palletsprojects.com/en/2.2.x/) and [Jinja](https://jinja.palletsprojects.com/en/3.1.x/).

## Dependencies

Create a virtual env and install dependencies with poetry: `poetry install`.

## Usage

Default usage: `poetry run python app.py` (development mode).

Open a browser to `localhost:5000`.

### Docker

Build image and run container: `docker-compose up --build -d app` (production mode).

Open a browser to `localhost:5000`.

See logs: `docker-compose logs -f app`.

Stop and remove container: `docker-compose down`.
