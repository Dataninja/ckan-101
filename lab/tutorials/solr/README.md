# CKAN 101 - Lab - Solr tutorial

A simple web app built on top of [Flask](https://flask.palletsprojects.com/en/2.2.x/), [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)
and [Solr](https://solr.apache.org/).

## Usage

Build images and run containers: `docker-compose up --build -d` (production mode).

Mount custom configuration: `docker-compose -f docker-compose.yml -f docker-compose.custom.yml up -d solr`.

### Database

Database initialization: `docker-compose exec app python db.py` (only the first time or after a docker-compose down).

Open a browser to `localhost:8983`.

### Web application

Open a browser to `localhost:5000`.

See logs: `docker-compose logs -f`.

Stop and remove containers: `docker-compose down`.
