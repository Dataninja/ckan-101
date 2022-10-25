#!/bin/bash

# Create DB tables if not there
# See https://github.com/ckan/ckanext-pages/tree/v0.3.7#database-initialization
echo "Ckanext Pages: INITDB"
ckan -c /srv/app/ckan.ini pages initdb
