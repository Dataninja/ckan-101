# #!/bin/bash

export CKAN_CONFIG=/srv/app
export CKAN_INI=$CKAN_CONFIG/ckan.ini
export CKANEXT_FOLDER=$CKAN_CONFIG/src/ckanext-dcatapit

# Populate controlled vocabularies (by EU and AgID)
# See https://github.com/geosolutions-it/ckanext-dcatapit#installation (n. 14)
echo "Ckanext Dcatapit: VOCABULARIES"
if [ ! -f "${CKANEXT_FOLDER}/vocabularies.downloaded" ]; then
  ckan -c $CKAN_INI dcatapit load --filename=$CKANEXT_FOLDER/vocabularies/languages-filtered.rdf
  ckan -c $CKAN_INI dcatapit load --filename=$CKANEXT_FOLDER/vocabularies/data-theme-filtered.rdf
  ckan -c $CKAN_INI dcatapit load --filename=$CKANEXT_FOLDER/vocabularies/places-filtered.rdf
  ckan -c $CKAN_INI dcatapit load --filename=$CKANEXT_FOLDER/vocabularies/frequencies-filtered.rdf
  ckan -c $CKAN_INI dcatapit load --filename=$CKANEXT_FOLDER/vocabularies/filetypes-filtered.rdf
  # curl https://raw.githubusercontent.com/italia/daf-ontologie-vocabolari-controllati/master/VocabolariControllati/territorial-classifications/regions/regions.rdf > regions.rdf
  # paster --plugin=ckanext-dcatapit vocabulary load --filename regions.rdf --name regions --config=/etc/ckan/default/production.ini
  ckan -c $CKAN_INI dcatapit load --filename=$CKANEXT_FOLDER/vocabularies/theme-subtheme-mapping.rdf --eurovoc $CKANEXT_FOLDER/vocabularies/eurovoc-filtered.rdf
  ckan -c $CKAN_INI dcatapit load --filename=$CKANEXT_FOLDER/vocabularies/licences.rdf

  touch $CKANEXT_FOLDER/vocabularies.downloaded
fi
