# #!/bin/bash

# Populate controlled vocabularies (by EU and AgID)
# See https://github.com/geosolutions-it/ckanext-dcatapit#installation (n. 14)
echo "Ckanext Dcatapit: VOCABULARIES"
if [ ! -f "/srv/app/src/ckanext-dcatapit/vocabularies.downloaded" ]; then
  ckan -c /srv/app/ckan.ini dcatapit load --filename=/srv/app/src/ckanext-dcatapit/vocabularies/languages-filtered.rdf
  ckan -c /srv/app/ckan.ini dcatapit load --filename=/srv/app/src/ckanext-dcatapit/vocabularies/data-theme-filtered.rdf
  ckan -c /srv/app/ckan.ini dcatapit load --filename=/srv/app/src/ckanext-dcatapit/vocabularies/places-filtered.rdf
  ckan -c /srv/app/ckan.ini dcatapit load --filename=/srv/app/src/ckanext-dcatapit/vocabularies/frequencies-filtered.rdf
  ckan -c /srv/app/ckan.ini dcatapit load --filename=/srv/app/src/ckanext-dcatapit/vocabularies/filetypes-filtered.rdf
  # curl https://raw.githubusercontent.com/italia/daf-ontologie-vocabolari-controllati/master/VocabolariControllati/territorial-classifications/regions/regions.rdf > regions.rdf
  # paster --plugin=ckanext-dcatapit vocabulary load --filename regions.rdf --name regions --config=/etc/ckan/default/production.ini
  ckan -c /srv/app/ckan.ini dcatapit load --filename=/srv/app/src/ckanext-dcatapit/vocabularies/theme-subtheme-mapping.rdf --eurovoc /srv/app/src/ckanext-dcatapit/vocabularies/eurovoc-filtered.rdf
  ckan -c /srv/app/ckan.ini dcatapit load --filename=/srv/app/src/ckanext-dcatapit/vocabularies/licences.rdf

  touch /srv/app/src/ckanext-dcatapit/vocabularies.downloaded
fi
