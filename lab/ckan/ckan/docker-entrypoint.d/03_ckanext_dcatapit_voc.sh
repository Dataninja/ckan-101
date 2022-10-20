# #!/bin/bash

# export CKAN_CONFIG=/srv/app
# export CKAN_INI=$CKAN_CONFIG/ckan.ini

# # Populate controlled vocabularies (by EU and AgID)
# # See https://github.com/geosolutions-it/ckanext-dcatapit#installation (n. 14)
# if [ ! -f "${CKAN_CONFIG}/vocabularies.downloaded" ]; then
#   ckan -c $CKAN_INI dcatapit load --filename=vocabularies/languages-filtered.rdf
#   ckan -c $CKAN_INI dcatapit load --filename=vocabularies/data-theme-filtered.rdf
#   ckan -c $CKAN_INI dcatapit load --filename=vocabularies/places-filtered.rdf
#   ckan -c $CKAN_INI dcatapit load --filename=vocabularies/frequencies-filtered.rdf
#   ckan -c $CKAN_INI dcatapit load --filename=vocabularies/filetypes-filtered.rdf
#   # curl https://raw.githubusercontent.com/italia/daf-ontologie-vocabolari-controllati/master/VocabolariControllati/territorial-classifications/regions/regions.rdf > regions.rdf
#   # paster --plugin=ckanext-dcatapit vocabulary load --filename regions.rdf --name regions --config=/etc/ckan/default/production.ini
#   ckan -c $CKAN_INI dcatapit load --filename vocabularies/theme-subtheme-mapping.rdf --eurovoc vocabularies/eurovoc-filtered.rdf
#   ckan -c $CKAN_INI dcatapit load --filename vocabularies/licences.rdf
# fi
