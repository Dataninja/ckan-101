# #!/bin/bash

export CKAN_CONFIG=/srv/app
export CKAN_INI=$CKAN_CONFIG/ckan.ini

# Create DB tables if not there
# See https://github.com/geosolutions-it/ckanext-multilang#installation (n. 3)
echo "Ckanext Multilang: INITDB"
ckan -c $CKAN_INI multilang initdb
