# #!/bin/bash

export CKAN_CONFIG=/srv/app
export CKAN_INI=$CKAN_CONFIG/ckan.ini

# Create DB tables if not there
# See https://github.com/geosolutions-it/ckanext-dcatapit#installation (n. 10)
echo "Ckanext Dcatapit: INITDB"
ckan -c $CKAN_INI dcatapit initdb
