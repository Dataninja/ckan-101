# #!/bin/bash

# Create DB tables if not there
# See https://github.com/geosolutions-it/ckanext-dcatapit#installation (n. 10)
echo "Ckanext Dcatapit: INITDB"
ckan -c /srv/app/ckan.ini dcatapit initdb
