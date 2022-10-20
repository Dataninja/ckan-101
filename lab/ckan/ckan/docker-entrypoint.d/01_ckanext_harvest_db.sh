#!/bin/bash

export CKAN_CONFIG=/srv/app
export CKAN_INI=$CKAN_CONFIG/ckan.ini

# Create DB tables if not there
# See https://github.com/ckan/ckanext-harvest/tree/v1.4.1#configuration
ckan -c $CKAN_INI harvester initdb
