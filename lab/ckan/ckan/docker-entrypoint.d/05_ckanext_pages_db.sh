#!/bin/bash

export CKAN_CONFIG=/srv/app
export CKAN_INI=$CKAN_CONFIG/ckan.ini

# Create DB tables if not there
# See https://github.com/ckan/ckanext-pages/tree/v0.3.7#database-initialization
echo "Ckanext Pages: INITDB"
ckan -c $CKAN_INI pages initdb
