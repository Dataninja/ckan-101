# Gestione dati

CKAN è un Data Management System il cui scopo principale è gestire metadati, cioè informazioni strutturate che descrivono altri dati.

## Metadati

La principale entità rappresentata da CKAN è il *dataset* (chiamato storicamente anche *package*) che contiene i metadati secondo uno schema proprietario, ma ormai divenuto uno *standard de facto*.

A ogni dataset possono essere associate delle risorse (chiamate *resources*) che contengono rappresentazioni dei dati veri e propri (descritti dai metadati). Possono essere file statici in vari formati (es. CSV, TSV, XLSX e JSON) o URL a risorse remote (es. web services).

> NOTA: se si vuole aderire agli standard internazionali su schemi e formati dei metadati, l'estensione `ckanext-dcat` (vedi [documentazione ufficiale](https://github.com/ckan/ckanext-dcat)) permette di gestirli ed esporli secondo lo standard [DCAT](https://www.w3.org/TR/vocab-dcat/) del W3C, adottato anche dall'Unione Europea (standard [DCAT_AP](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe/release/211)) e dall'Italia (standard [DCAT_AP-IT](https://www.dati.gov.it/content/dcat-ap-it-v10-profilo-italiano-dcat-ap-0)).

### Filestore

Il plugin `filestore` integrato in CKAN e attivato di default permette di creare risorse caricando file statici (es. CSV) che l'utente finale può scaricare (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/maintaining/filestore.html)).

## Datastore

Il plugin `datastore` integrato in CKAN e attivabile a richiesta permette di indicizzare all'interno del database anche il contenuto dei file caricati nelle risorse (es. CSV) così che l'utente finale può non solo scaricare i file originari, ma anche interrogarli direttamente (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/maintaining/datastore.html)).

### Datapusher

Il plugin `datapusher` integrato in CKAN e attivabile a richiesta, ma che richiede l'esecuzione di un [servizio aggiuntivo](https://github.com/ckan/datapusher), permette di automatizzare l'inserimento del contenuto dei file caricati come risorse nel Filestore all'interno del Datastore (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/maintaining/datastore.html#datapusher-automatically-add-data-to-the-datastore)).

## Harvesting

Un'istanza di CKAN può popolare automaticamente il proprio catalogo a partire da cataloghi di altre istanze di CKAN (o che espongono API compatibili con quelle di CKAN, come nel caso di [DKAN](https://getdkan.org/)).

In questo modo si trasforma in una sorta di meta-catalogo che raccoglie e aggrega altri cataloghi e li rende ricercabile in un unico luogo (es. [www.dati.gov.it](https://www.dati.gov.it/)).

Il processo di importazione e sincronizzazione di cataloghi tra istanze di CKAN si chiama `harvesting` ed è implementato dall'estensione `ckanext-harvest` (vedi [documentazione ufficiale](https://github.com/ckan/ckanext-harvest)).

## Anteprime e visualizzazioni dati

Nelle pagine delle risorse l'utente può scaricare il file caricato oppure seguire il link alla risorsa remota grazie al `filestore`.

Se è attivo il `datastore` può anche visualizzare un'anteprima interattiva della risorsa grazie alle viste (*views*) eventualmente configurate (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/maintaining/data-viewer.html)).

Le viste sono opzionali e quelle di default sono `image_view` e `text_view`. Se il datastore è attivo, si può aggiungere anche la vista `recline_view` che permette all'utente di visualizzare i dati tabellari sotto forma di tabella ricercabile e filtrabile, come grafico o come mappa.

Le estensioni possono fornire anche nuove viste, come per esempio `ckanext-geoview` (vedi [documentazione ufficiale](https://github.com/ckan/ckanext-geoview)).

## Dati geospaziali

I tipici formati dati dei Sistemi Informativi Geografici ([GIS](https://en.wikipedia.org/wiki/Geographic_information_system)) possono essere gestiti nativamente grazie all'estensione `ckanext-spatial` (vedi [documentazione ufficiale](https://github.com/ckan/ckanext-spatial)), che estende il datastore sfruttando le funzionalità geografiche del database [PostGIS](https://postgis.net/).

Per esempio è possibile associare informazioni geografiche ai dataset e offrire un motore di ricerca per luoghi (vedi [documentazione ufficiale](https://docs.ckan.org/projects/ckanext-spatial/en/latest/spatial-search.html)).

## Application Programming Interface (API REST)

Quella grafica è l'interfaccia principale per la fruizione e gestione manuale dei contenuti di CKAN.

CKAN mette a disposizione anche un ricco e completo set di API (chiamate `Action API`, vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/api/index.html)) per accedere a dati e metadati, oltre che per la gestione dei contenuti nel caso di richieste opportunamente autenticate.

Esempio: [curl localhost:5000/api/3/action/package_list](http://localhost:5000/api/3/action/package_list).
