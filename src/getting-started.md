# Primi passi

Il codice sorgente di CKAN è pubblicato su Github: https://github.com/ckan/ckan.

La [guida ufficiale](https://docs.ckan.org/en/2.9/maintaining/installing/install-from-docker-compose.html) per l'installazione e l'esecuzione di CKAN in ambiente Docker utilizza configurazioni datate di [docker-compose.yml](https://github.com/ckan/ckan/blob/ckan-2.9.6/contrib/docker/docker-compose.yml) e `Dockerfile` (ambiente Python2 invece di Python3, Solr v6 invece di v8, immagine di [datapusher](https://hub.docker.com/r/clementmouchet/datapusher) su Docker Hub molto vecchia rispetto alle [ultime versioni dei sorgenti](https://github.com/ckan/datapusher) su Github).

Le configurazioni presentate in questo corso partono da quelle della Open Knowledge Foundation: [okfn/docker-ckan](https://github.com/okfn/docker-ckan) (vedi anche [tech.datopian.com/ckan](https://tech.datopian.com/ckan/)) con alcune modifiche.

## Servizi e container

I servizi sono CKAN, Postgis, Solr, Redis e Datapusher. Le estensioni attivate di default sono il [Datastore](https://docs.ckan.org/en/2.9/maintaining/datastore.html) e [Datapusher](https://docs.ckan.org/en/2.9/maintaining/datastore.html#datapusher-automatically-add-data-to-the-datastore).

> ATTENZIONE: la preview delle risorse non funzionerà in locale (es. localhost:5000) per un limite della configurazione di Datapusher (vedi [okfn/docker-ckan#73](https://github.com/okfn/docker-ckan/issues/73)).

### Postgis

Servizio `db` nel `docker-compose.yml`, l'immagine si basa su [postgis/postgis:15-3.3-alpine](https://hub.docker.com/r/postgis/postgis). Durante la build dell'immagine (`Dockerfile` in `lab/ckan/postgresql`) vengono caricati gli script di inizializzazione in `docker-entrypoint-initdb.d/`.

### CKAN

Servizio `ckan` nel `docker-compose.yml`, l'immagine si basa su [openknowledge/ckan-base:2.9](https://hub.docker.com/r/openknowledge/ckan-base).

### Redis

Servizio `redis` nel `docker-compose.yml`, basato sull'immagine ufficiale di [redis:7-alpine](https://hub.docker.com/_/redis).

### Solr

Servizio `solr` nel `docker-compose.yml`, l'immagine si basa su [ckan/ckan-solr:2.9-solr8](https://hub.docker.com/r/ckan/ckan-solr).

### Datapusher

Servizio `datapusher` nel `docker-compose.yml`, basato su un'immagine personalizzata in `lab/ckan/datapusher` basata su [alpine:3.15](https://hub.docker.com/_/alpine) riferita alla versione [0.0.18](https://github.com/ckan/datapusher/tree/0.0.18) dei sorgenti.

## Orchestrazione dei container

A partire dal file di configurazione `dcker-compose.yml` della cartella `lab/ckan/` è possibile costruire le immagini di tutti i servizi con `docker-compose build` ed eseguirne i relativi container con `docker-compose up`.

Prima però è necessario configurare le variabili d'ambiente globali (file `.env`) e i volumi per la persistenza dei dati.

> TIP: nel caso si debbano eseguire comandi mediante la CLI di CKAN, bisogna farlo all'interno del container in esecuzione mediante `docker-compose exec ckan [comando]`. Esempio: `docker-compose exec ckan ckan -c /srv/app/ckan.ini sysadmin add user_name`.

### Variabili d'ambiente

Il [file ufficiale](https://github.com/okfn/docker-ckan/blob/master/.env.example) di configurazione (in `lab/ckan/.env.example`) è replicato e modificato in `lab/ckan/.env` e caricato da Docker Compose durante la fase di build delle immagini e all'esecuzione dei container.

> ATTENZIONE: normalmente il file `.env` contiene informazioni riservate, per cui non è incluso nel repository pubblico (compare nel file `.gitignore`). Bisogna duplicare il file `.env.example` manualmente e modificarlo opportunamente. In questo repository è incluso solo per fini didattici.

CKAN usa l'estensione [ckanext-envvars](https://github.com/okfn/ckanext-envvars) per compilare il file di configurazione `ckan.ini` a partire dalle variabili d'ambiente valorizzate nel file `.env`. In generale le opzioni del tipo `ckan.extension.option_1` sono tradotte in `CKAN__EXTENSION__OPTION_1` (`__` al posto di `.` e tutto maiuscolo). Per i dettagli si veda la [documentazione ufficiale](https://github.com/okfn/ckanext-envvars).

#### Mail server
CKAN può inviare mail transazionali (es. per la registrazione o l'invito di nuovi utenti) solo se viene configurato opportunamente un servizio mail esterno mediante il protocollo SMTP. Si veda la sezione dedicata nel file `.env`.

### Volumi

Sezione `volumes` nel `docker-compose.yml`. Per impostazione predefinita i volumi sono definiti come [docker named volumes](https://docs.docker.com/storage/volumes/), ma volendo possono essere montati su cartelle locali dell'host.

#### CKAN Storage

Volume con i file delle risorse e le eventuali immagini caricate (cartella interna al container: `/var/lib/ckan`).

#### Postgres data

Volume per la persistenza dei dati del database principale (cartella interna al container: `/var/lib/postgresql/data`).

#### Solr data

Volume per la persistenza dei dati del motore di ricerca (cartella interna al container: `/opt/solr/server/solr/ckan/data/index`).

## Avvio

Gli script della configurazione iniziale si occupano di inizializzare la nuova installazione in base alle configurazioni contenute nel file `.env` (es. le credenziali dell'utente di amministrazione).

Per configurazioni avanzate le opzioni sono gestite dall'estensione [okfn/ckanext-envvars](https://github.com/okfn/ckanext-envvars), attivata di default (es. `CKAN__LOCALE_DEFAULT=it`).

Build delle immagini: `docker-compose build` in `lab/ckan/`.

Esecuzione della versione base: `docker-compose up -d`.

Accesso ai log: `docker-compose logs -f`.

Il sito è visibile all'indirizzo [localhost:5000](http://localhost:5000).

## Gestione delle utenze

Per impostazione predefinita CKAN permette a chiunque di registrarsi, previa configurazione di un servizio di posta e l'attivazione dell'account da parte di un utente amminstratore. Si può disabilitare questa opzione configurando la variabile d'ambiente `CKAN__AUTH__CREATE_USER_VIA_WEB=False` nel file `.env`.

L'utente amministratore può invitare un utente a registrarsi a partire dalla sua mail, purché il servizio di posta sia correttamente configurato.

L'utente amministratore può creare direttamente nuovi utenti (amministratori o no) mediante linea di comando:

- nuovo amministratore: `docker-compose exec ckan ckan -c /srv/app/ckan.ini sysadmin add ckan_admin_2 email=ckan_admin_2@localhost name=ckan_admin_2`
- nuovo utente semplice: `docker-compose exec ckan ckan -c /srv/app/ckan.ini user add ckan_1 email=ckan_1@localhost name=ckan_1`

Per ulteriori dettagli si veda la [documentazione ufficiale](https://docs.ckan.org/en/2.9/sysadmin-guide.html#creating-a-sysadmin-account).

## Backup

È sufficiente sottoporre a backup i tre volumi persistenti, in particolare `pg_data` e `ckan_storage`.

Nel caso del database è possibile utilizzare gli strumenti nativi di PostgreSQL come `pg_dump` e `pg-restore` (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/maintaining/database-management.html#import-and-export)):

- dump: `docker-compose exec db pg_dump -Fc -U ckan -d ckan > ckan.dump`
- restore: `docker-compose exec db pg_restore --clean --if-exists -U ckan -d ckan < ckan.dump`

## Aggiornamento

È sempre consigliato indicare esplicitamente le versioni delle immagini docker o le tag dei repository da cui si dipende, per controllare eventuali aggiornamenti.

Leggere sempre i CHANGELOG prima di effettuare un aggiornamento (es. per [ckan 2.9](https://docs.ckan.org/en/2.9/changelog.html)), seguendo la [documentazione ufficiale](https://docs.ckan.org/en/2.9/maintaining/upgrading/index.html) in merito.

A questo punto è sufficiente modificare le versioni indicate nei file rilevanti (es. `docker-compose.yml` e/o `Dockerfile`) e rifare la build delle immagini (es. `docker-compose up --build -d`).

## Localizzazione

CKAN è già distribuito con [decine di lingue](https://docs.ckan.org/en/2.9/contributing/i18n.html) e per impostazione predefinita l'utente può scegliere quella che preferisce da un menù a tendina (l'inglese è la lingua predefinita).

> ATTENZIONE: la versione qui presentata ha impostata la lingua italiana come lingua di default (vedi variabile `CKAN__LOCALE_DEFAULT=it` file `.env`).
