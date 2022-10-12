# CKAN 101 - Lab - Python tutorial

A simple hello world script.

## Usage

Default usage: `python main.py`.

Advanced usage: `python main.py [subject]` (ie. `python main.py friends`).

Execution in docker container: `docker run -it --rm --name lab_python_1 -v $PWD/main.py:/opt/main.py python:3.9 python /opt/main.py friends`.
