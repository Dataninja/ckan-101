# Estensioni

Le funzionalità di CKAN possono essere ampliate mediante estensioni (dette `ckanext`), alcune delle quali sono ufficiali, perché mantenute dal core team di CKAN (es. [ckan/repositories?q=ckanext-](https://github.com/orgs/ckan/repositories?q=ckanext-&type=all&language=&sort=)), altre di terze parti (vedi [extensions.ckan.org](https://extensions.ckan.org/)).

> ATTENZIONE: la versione 2.9 di CKAN presentata in questo repository viene eseguita in ambiente Python3, per cui eventuali vecchie estensioni che supportano solo Python2 non sono compatibili.

In questo repository l'installazione, l'inizializzazione, la configurazione delle estensioni viene effettuata nel file `/lab/ckan/ckan/Dockerfile.ext` (usato dal file `docker-compose.ext.yml`) e la loro attivazione del file `.env`.

## Estensioni built-in

Alcune estensioni sono già presenti nel core di CKAN (si veda la cartella `ckanext` del [repository ufficiale](https://github.com/ckan/ckan/tree/master/ckanext)), quindi vanno semplicemente attivati i plugin che forniscono nel file `.env` aggiungendoli in coda alla variabile `CKAN__PLUGINS` e poi riavviando il container con `docker-compose up -d ckan`.

Alcune estensioni mettono a disposizione anche delle *viste* (`views`), delle modalità di preview delle risorse. In tal caso vanno esplicitamente attivate mediante la variabile `CKAN__VIEWS__DEFAULT_VIEWS` nel file `.env`. Si rimanda alla documentazione delle singole estensioni per i dettagli.

## Estensioni ufficiali e di terze parti

Le estensioni ufficiali e di terze parti sono rilasciate come pacchetti Python e vanno installate e attivate opportunamente, in generale sono necessari i seguenti passaggi:

1. installare l'estensione mediante `pip`, spesso direttamente dal repository pubblico su Github (es. `pip install -e git+https://github.com/ckan/ckanext-pages.git#egg=ckanext-pages`);
2. [opzionale] installare eventuali pacchetti aggiuntivi richiesti (es. `pip install -r https://raw.githubusercontent.com/ckan/ckanext-dcat/v0.0.6/requirements.txt`);
3. [opzionale] eseguire eventuali script di inizializzazione del database;
4. [opzionale] eseguire eventuali script di inizializzazione mediante la CLI di CKAN;
5. attivare l'estensione e aggiungere eventuali configurazioni specifiche;
6. riavviare CKAN.

Nella versione dockerizzata di questo repository questi passaggi si traducono nella seguente procedura:

1. aggiungere le istruzioni di installazione dell'estensione e dei requisiti al file `lab/ckan/ckan/Dockerfile.ext` (vedi esempi);
3. [opzionale] aggiungere un eventuale script di inizializzazione del database in `lab/ckan/postgresql/docker-entrypoint-initdb.d`;
4. [opzionale] aggiungere un eventuale script di inizializzazione in `lab/ckan/ckan/docker-entrypoint.d`;
5. aggiungere i plugin forniti dall'estensione all'elenco della variabile d'ambiente `CKAN__PLUGINS` nel file `.env` e le eventuali configurazioni aggiuntive;
6. rifare la build delle immagini e riavviare i container con `docker-compose -f docker-compose.yml -f docker-compose.ext.yml up --build -d`.

### Rimozione

Per rimuovere un plugin precedentemente attivato è necessario ripercorrere a ritroso i passaggi per la sua installazione, dal punto 5 al punto 1.
Infine rifare la build delle immagini e riavviare i container.

> ATTENZIONE: alcune estensioni potrebbero inizializzare il database creando tabelle aggiuntive, fare sempre riferimento alla documentazione ufficiale dell'estensione per capire se è prevista un'opportuna procedura di pulizia post-rimozione.

> ATTENZIONE: alcune estensioni dipendono da altre estensioni (es. dcatapit da dcat), fare sempre riferimento alle documentazioni ufficiali.

## Laboratorio

Installiamo e configuriamo un portale completo in accordo con le [linee guida AgID](https://docs.italia.it/italia/daf/lg-patrimonio-pubblico/it/stabile/index.html).

Estensioni attivate:

- [Pages](https://github.com/ckan/ckanext-pages)
- [Harvest](https://github.com/ckan/ckanext-harvest)
- [Spatial](https://github.com/ckan/ckanext-spatial)
- [Geoview](https://github.com/ckan/ckanext-geoview)
- [DCAT](https://github.com/ckan/ckanext-dcat)
- [Multilang](https://github.com/geosolutions-it/ckanext-multilang)
- [DCAT_AP-IT](https://github.com/geosolutions-it/ckanext-dcatapit)
