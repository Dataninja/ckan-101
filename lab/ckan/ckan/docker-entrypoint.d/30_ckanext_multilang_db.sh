# #!/bin/bash

# Create DB tables if not there
# See https://github.com/geosolutions-it/ckanext-multilang#installation (n. 3)
echo "Ckanext Multilang: INITDB"
ckan -c /srv/app/ckan.ini multilang initdb
