# Primi passi

Il codice sorgente di CKAN è pubblicato su Github: https://github.com/ckan/ckan.

All'interno del [repository di questo corso](https://github.com/Dataninja/ckan-101) è presente nella cartella `lab/modules/ckan` sotto forma di [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

Se hai clonato il repository con `git clone https://github.com/Dataninja/ckan-101.git` puoi *popolare* la cartella `lab/modules/ckan` con la [versione ckan-2.9.6](https://github.com/ckan/ckan/tree/ckan-2.9.6) con i comandi `git submodule init` e `git submodule update`.

> ATTENZIONE: la [guida completa](https://docs.ckan.org/en/2.9/maintaining/installing/install-from-docker-compose.html) per l'installazione e l'esecuzione di CKAN in ambiente Docker utilizza configurazioni datate di `docker-compose.yml` e `Dockerfile` (ambiente Python2 invece di Python3, Solr v6 invece di v8, una vecchia immagine di Datapusher).

Le configurazioni presentate in questo corso partono da quelle ufficiali, ma aggiornano tutte le dipendenze alle ultime versioni disponibili / compatibili.

## Servizi e container

Il [docker-compose.yml](https://github.com/ckan/ckan/blob/ckan-2.9.6/contrib/docker/docker-compose.yml) ufficiale (in `lab/modules/ckan/contrib/docker/`) è replicato e modificato in `lab/docker-compose.yml`.

### Database (PostGIS)

Servizio `db` nel `docker-compose.yml`. Fa uso del [Dockerfile ufficiale](https://github.com/ckan/ckan/blob/ckan-2.9.6/contrib/docker/postgresql/Dockerfile) (in `lab/modules/ckan/contrib/docker/postgresql`) e l'immagine si basa su [postgis:11](https://hub.docker.com/r/mdillon/postgis/).

### CKAN

Servizio `ckan` nel `docker-compose.yml`. Fa uso del [Dockerfile ufficiale](https://github.com/ckan/ckan/blob/ckan-2.9.6/Dockerfile.py3) (in `lab/modules/ckan/Dockerfile.py3`) e l'immagine si basa su [ubuntu:focal](https://hub.docker.com/_/ubuntu).

### Redis

Servizio `redis` nel `docker-compose.yml`, basato sull'[immagie ufficiale](https://hub.docker.com/_/redis).

### Solr

Servizio `solr` nel `docker-compose.yml`. Fa uso di un Dockerfile personalizzato (in `lab/services/solr/`) basato sull'immagine ufficiale [ckan/ckan-solr:2.9-solr8](https://hub.docker.com/r/ckan/ckan-solr).

### Datapusher

...

## Orchestrazione dei container

A partire dai file di configurazione di Docker Compose della cartella `lab/` è possibile costruire le immagini di tutti i servizi con `docker-compose build` ed eseguirne i relativi container con `docker-compose up`.

Prima però è necessario configurare le variabili d'ambiente globali (file `.env`), i volumi per la persistenza dei dati e la personalizzazione delle configurazioni e le porte esposte dei vari servizi.

### Variabili d'ambiente

Il [file ufficiale](https://github.com/ckan/ckan/blob/ckan-2.9.6/contrib/docker/.env.template) di configurazione (in `lab/modules/ckan/contrib/docker/.env.template`) è replicato e compilato in `lab/.env` e caricato da Docker Compose durante la fase di build delle immagini e all'esecuzione dei container.

### Volumi

Sezione `volumes` nel `docker-compose.yml`. Per impostazione predefinita i volumi sono definiti come [docker named volumes](https://docs.docker.com/storage/volumes/), ma volendo possono essere montati su cartelle locali dell'host.

#### CKAN Config

Volume con la configurazione principale di CKAN, in particolare contiene il file `production.ini` (cartella interna al container: `/etc/ckan`).

In caso di personalizzazione della configurazione (es. attivazione di estensioni o opzioni avanzate nel file `production.ini`) è utile montare un file modificabile usando anche la configurazione in `docker-compose.custom.yml` con `docker-compose -f docker-compose.yml -f docker-compose.custom.yml up -d ckan`.

#### CKAN Home

Volume con il codice sorgente e le eventuali estensioni aggiuntive (cartella interna al container: `/usr/lib/ckan`).

#### CKAN Storage

Volume con i file delle risorse e le eventuali immagini caricate (cartella interna al container: `/var/lib/ckan`).

#### Postgres data

Volume per la persistenza dei dati del database principale (cartella interna al container: `/var/lib/postgresql/data`).

#### Solr data

Volume per la persistenza dei dati del motore di ricerca (cartella interna al container: `/opt/solr/server/solr/ckan/data`).

In caso di personalizzazione della configurazione (es. opzioni avanzate nel file `schema.xml`) è utile montare un file modificabile usando anche la configurazione in `docker-compose.dev.yml` con `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d solr`.

## Configurazione iniziale

### Utente di amministrazione

L'installazione iniziale richiede la creazione diretta di un utente di amministrazione che poi potrà effettura il primo login e configurare il sito dall'interfaccia web.

Eseguire `docker-compose exec -T ckan /usr/local/bin/ckan -c /etc/ckan/production.ini sysadmin add ckanadmin`.

### Datastore

Per avere la possibilità di caricare file come risorse è necessario attivare il [Datastore](https://docs.ckan.org/en/2.9/maintaining/installing/install-from-docker-compose.html#datastore-and-datapusher). Questo richiede una inizializzazione aggiuntiva del database e l'attivazione nel file di configurazione `production.ini`.

Inizializzazione: `docker-compose exec ckan /usr/local/bin/ckan -c /etc/ckan/production.ini datastore set-permissions | docker-compose exec -T db psql -U ckan`.

Per l'attivazione è necessario montare nel container `ckan` una versione modificabile del file `production.ini` (in `lab/services/ckan/`) e riavviare il servizio: `docker-compose -f docker-compose.yml -f docker-compose.custom.yml up -d ckan`.

## Backup

...

## Aggiornamento

...

## Localizzazione

...
