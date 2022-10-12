# CKAN 101 - Lab - PostGIS tutorial

A simple web app built on top of [Flask](https://flask.palletsprojects.com/en/2.2.x/), [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
and [PostGIS](http://postgis.net/).

## Usage

Build images and run containers: `docker-compose up --build -d` (production mode).

### Database

Database initialization: `docker-compose exec app python db.py` (only the first time or after a docker-compose down).

Open a browser to `localhost:8080` (use credentials in `docker-compose.yml` and `.env` files).

### Web application

Open a browser to `localhost:5000`.

See logs: `docker-compose logs -f`.

Stop and remove containers: `docker-compose down`.
