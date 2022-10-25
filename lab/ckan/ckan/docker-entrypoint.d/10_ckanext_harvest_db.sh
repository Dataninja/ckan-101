#!/bin/bash

# Create DB tables if not there
# See https://github.com/ckan/ckanext-harvest/tree/v1.4.1#configuration
echo "Ckanext Harvest: INITDB"
ckan -c /srv/app/ckan.ini harvester initdb
