# CKAN 101 - Lab - React tutorial

A simple static page on top of [React](https://reactjs.org/),
and [Create React App](https://create-react-app.dev/) and [nginx](https://www.nginx.com/).

## Usage

### Production

Build image and run container: `docker-compose up --build -d` (production mode).

Open a browser to `localhost:8080`.

See logs: `docker-compose logs -f`.

Stop and remove containers: `docker-compose down`.

### Development

Build image and run container: `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build -d` (development mode).

Open a browser to `localhost:3000` and edit `src/App.js` file (live reload!).

See logs: `docker-compose logs -f`.

Stop and remove containers: `docker-compose down`.
