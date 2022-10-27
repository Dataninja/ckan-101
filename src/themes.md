# Temi

Per personalizzare l'interfaccia grafica di CKAN è necessario sviluppare un'estensione che modifichi i template forniti dall'installazione ufficiale basati su [Jinja](https://jinja.palletsprojects.com/en/3.1.x/).

## Tema built-in

L'unica personalizzazione possibile del tema predefinito di CKAN è la palette di colori, modificabile come utente amministratore nella pagina di configurazione (`/ckan-admin/config`) sotto la voce "Stile".

Colori disponibili:

- blu (default),
- rosso chiaro,
- verde,
- rosso scuro,
- fucsia.

Nella stessa pagina è inoltre possibile personalizzare gli elementi in homepage selezionando una delle opzioni sotto la voce "Homepage":

- Introductory area, search, featured group and featured organization
- Search, stats, introductory area, featured organization and featured group
- Search, introductory area and stats

Per piccole modifiche allo stile delle pagine è possibile salvare un codice CSS personalizzato nella pagina di configurazione (`/ckan-admin/config`) sotto la voce "CSS personalizzato". Si tratta di regole CSS globali, caricate in tutte le pagine, per cui è importante definire selettori abbastanza specifici su classi e id.

Esempio per nascondere l'immagine in homepage nella card di benvenuto: `.homepage .featured { display: none; }`.

È anche possibile impostare una favicon personalizzata valorizzando la variabile d'ambiente `CKAN__FAVICON` con un url assoluto a una risorsa esterna (ed. `CKAN__FAVICON=https://www.estar.toscana.it/wp-content/uploads/2021/04/Logo-Estar_150x150.png`).

## Temi di terze parti

Un tema di CKAN è un'estensione, quindi se rilasciata in open source si può scaricare e installare (vedi la [sezione sulle estensioni](./extensions)).

È molto difficile però scrivere un tema personalizzabile e abbastanza flessibile da essere riutilizzato, quindi se ne trovano molto pochi.

## Sviluppo di un tema

Lo sviluppo di un tema personalizzato richiede l'inizializzazione di un'estensione con le opportune configurazioni, la creazione e modifica dei template di pagina, del CSS e del Javascript, la gestione della localizzazione delle stringhe all'interno dei template e del codice Javascript.

Vengono in aiuto alcuni comandi della CLI di CKAN che permettono di inizializzare un'estensione vuota adatta allo scopo, di eseguire CKAN in modalità sviluppo con una serie di utility pre-caricate, di gestire la localizzazione delle stringhe.

La [documentazione ufficiale](https://docs.ckan.org/en/2.9/extensions/tutorial.html) mostra lo sviluppo da zero di un'estensione all'interno di un tutorial per spiegare i vari passaggi necessari per estendere le funzionalità di CKAN.

Nel nostro caso, la Open Knowledge Foundation descrive una [modalità di sviluppo](https://github.com/okfn/docker-ckan#development-mode) direttamente all'interno di un container ottimizzato per questo scopo.

1. Fare la build dell'immagine di sviluppo: `docker-compose -f docker-compose.yml -f docker-compose.dev.yml build ckan`
2. Eseguire i container in modalità sviluppo: `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d`
3. Inizializzare la nuova estensione: `docker-compose -f docker-compose.yml -f docker-compose.dev.yml exec ckan ckan generate extension --output-dir /srv/app/src_extensions`

Rispondere a tutte le domande poste:

1. Nome dell'estensione (deve iniziare con `ckanext-`, es. `ckanext-estar`)
2. Nome dell'autore
3. E-mail dell'autore
4. Nome utente o organizzazione su Github
5. Descrizione dell'estensione
6. Tag

Nella cartella locale `lab/ckan/src` apparirà la cartella della nuova estensione con il nome scelto al punto 1 (es. `lab/ckan/src/ckanext-estar`).

Per modificarne i file all'interno è forse necessario modificare opportunamente i permessi della cartella.

4. Aggiungere alla variabile d'ambiente `CKAN__PLUGINS` il nome del plugin fornito dall'estensione appena creata (es. `CKAN__PLUGINS=... nome_nuova_estensione` senza il prefisso `ckanext-`).
5. Riavviare il container: `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d ckan`.

La versione di CKAN in esecuzione raggiungibile all'indirizzo `localhost:5000` è ora in modalità sviluppo, per cui l'interfaccia presenta degli elementi interattivi che contengono informazioni di debug:

- in alto a sinistra ci sono *Controller* e *Action* utilizzati dalla pagina corrente;
- in basso nel footer c'è una sezione nascosta, ma visibile cliccando sul messaggio *Debug*;
- a destra c'è un menu di debug con una serie di risorse visibili cliccando sulle varie voci.

### Panoramica di un'estensione

Nella cartella appena creata in `lab/ckan/src/ckanext-estar` ci sono vari file pre-configurati:

- `README.md` contiene un modello di documentazione raccomandato per l'estensione
- `setup.py` contiene la definizione dell'estensione con le informazioni indicate interattivamente durante la creazione, è bene verificare che tutte le informazioni siano corrette e aggiornate
- `setup.cfg` contiene configurazioni di default per [Babel](https://babel.pocoo.org/en/latest/), il gestore della localizzazione delle stringhe
- `requirements.txt` contiene gli eventuali pacchetti aggiuntivi da cui l'estensione dipende

Nella sotto cartella `ckanext/estar/` c'è il vero e proprio codice che implementa le funzionalità dell'estensione:

- `plugin.py` contiene la definizione dei plugin offerti dall'estensione, sotto forma di classi che ereditano da `ckan.plugins.SingletonPlugin`
- `public/` contiene i file statici che saranno serviti a partire dalla root del sito (es. fogli di stile, immagini, ecc.)
- `templates/` contiene i template di pagina secondo la [struttura originaria](https://github.com/ckan/ckan/tree/master/ckan/templates)
- `fanstatic/` contiene i file Javascript caricati dall'estensione (es. per le funzionalità di un widget)
- `i18n/` contiene i file di localizzazione delle stringhe

> ATTENZIONE: le classi definite in `plugin.py` devono essere opportunamente elencate anche nel file `setup.py` nella variabile `entry_points`

### File statici

Qualsiasi file in `public/` sarà pubblicato a partire dalla root del sito (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/static-files.html)).
Per esempio il file `public/images/favicon.png` sarà raggiungibile all'indirizzo `localhost:5000/images/favicon.png`.

### Template di pagina personalizzati

CKAN usa Jinja come motore di template e fa ampio uso del concetto di *composizione*.
Si parte dai [template di base](https://github.com/ckan/ckan/tree/2.9/ckan/templates) definiti da CKAN e si sovrascrivono o si estendono opportunamente, andando a modificare solo le parti di interesse (i *blocks*).

Per esempio, se è attivo il primo layout "Introductory area, search, featured group and featured organization" e si crea un file `templates/home/layout1.html` vuoto, questo sovrascriverà interamente l'[originale](https://github.com/ckan/ckan/blob/2.9/ckan/templates/home/layout1.html) e in homepage non si vedrà più il corpo centrale della pagina.

> ATTENZIONE: a volte l'aggiunta di un nuovo template non ha effetti sulla pagina del sito, probabilmente a causa della cache delle pagine. Aspettare oppure fare un restart del container con `docker-compose -f docker-compose.yml -f docker-compose.dev.yml restart ckan`.

Se invece di sostituire un template, lo si vuole estendere, è sufficiente inserire in testa al file il codice `{% ckan_extends %}` (un *tag* nel linguaggio di Jinja, si veda la [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/templates.html#extending-templates-with-ckan-extends)).

```
{% ckan_extends %}
```

I template possono definire dei tag *block* che possiedono un nome univoco e che possono essere sovrascritti indipendentemente dal resto.

Per esempio, per rimuovere solo il riquadro con il testo di introduzione dalla homepage è sufficiente sovrascrivere il solo block `promoted` del `layout1.html` aggiungendo all'omonimo file dell'estensione il codice `{% block promoted %}{% endblock %}` (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/templates.html#replacing-template-blocks-with-block)).

```
{% ckan_extends %}

{% block promoted %}{% endblock %}
```

Se invece di sostituire del tutto il contenuto di un blocco si volesse estenderlo aggiungendo elementi prima o dopo il contenuto originale, si può usare la variabile `{{ super() }}` (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/templates.html#extending-parent-blocks-with-jinja-s-super)).

```
{% ckan_extends %}

{% block promoted %}
<p>Intestazione</p>
{{ super() }}
<p>Piè di blocco</p>
{% endblock %}
```

All'interno dei template si possono definire delle variabili e poi utilizzarle all'interno delle *espressioni*.
Alcune variabili notevoli sono definite a livello globale, come `app_globals`, accessibile anche con l'alias `g` (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/templates.html#expressions-and-variables)).

```
{% ckan_extends %}

{% block promoted %}
<p>Intestazione di {{ g.site_title }}</p>
{{ super() }}
<p>Piè di blocco</p>
{% endblock %}
```

Al pari delle variabili, che vengono semplicemente stampate, nelle espressioni si possono usare metodi che vengono eseguiti.
Si chiamano *helper functions*, [ce ne sono molte pre-definite](https://docs.ckan.org/en/2.9/theming/template-helper-functions.html) e possono essere definite all'interno di un'estensione nel file `plugin.py`.

```diff
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
+from random import randrange

+def random_integer():
+    return randrange(1, 10)

class EstarThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
+    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'estar')

+    def get_helpers(self):
+        return {
+            "estar_random_integer": random_integer
+        }
```

Tutte le variabili e le funzioni accessibili globalmente nei template sono elencate e descritte nella [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/variables-and-functions.html).

I tag di Jinja supportano un sotto insieme delle funzionalità di Python, per esempio ci sono i cicli e i blocchi condizionali.
Si possono anche usare tutti i metodi dei tipi di Python, come quelli di stringhe, liste e dizionari.
La concatenazione di funzioni si fa con la `|` (pipe).

Esempio completo per il file `layout1.html`.

```
{% ckan_extends %}

{% block promoted %}
<p>Intestazione di {{ g.site_title }}</p>
{{ super() }}
{% set random_integer = h.estar_random_integer() %}
<p>Piè di blocco n. {{ (random_integer / 2) | int }}</p>
<ul>
  {% for n in range(random_integer) %}
  {% if n % 2 %}
  <li>{{ n }}</li>
  {% endif %}
  {% endfor %}
</ul>
{% endblock %}
```

### CSS personalizzato

Per l'inclusione di fogli di stile nelle pagine si può sovrascrivere il blocco `styles` del template `base.html`, quello utilizzato da tutte le pagine del sito, per far caricare un file statico nella cartella `public/`.

```
{% ckan_extends %}

{% block styles %}
  {{ super() }}
  <link rel="stylesheet" href="/css/estar.css" />
{% endblock %}
```

> ATTENZIONE: recentemente è stato introdotto un metodo più avanzato per l'inclusione di CSS personalizzato che fa uso di [Webassets](https://webassets.readthedocs.io/en/latest/), si rimanda alla [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/webassets.html) per tutti i dettagli.

### Traduzioni personalizzate

Il supporto per la localizzazione non è attivo di default, per cui bisogna modificare il file `plugin.py` (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/extensions/translating-extensions.html)).

```diff
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
+from ckan.lib.plugins import DefaultTranslation
from random import randrange

def random_integer():
    return randrange(1, 10)

-class EstarThemePlugin(plugins.SingletonPlugin):
+class MyCustomThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
+    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'estar')

    def get_helpers(self):
        return {
            "estar_random_integer": random_integer
        }
```

Nei template ora è possibile usare le espressioni `{% trans %}{% endtrans %}` o la funzione `{{ _('') }}` per la localizzazione (vedi [documentazione ufficiale](https://docs.ckan.org/en/2.9/contributing/string-i18n.html#internationalizating-strings-in-jinja2-templates)).

Per esempio, nel template `layout1.html`.

```
{% ckan_extends %}

{% block promoted %}
<p>{% trans %}block header{% endtrans %}: {{ g.site_title }}</p>
{{ super() }}
{% set random_integer = h.estar_random_integer() %}
<p>{{ _('block footer') }} #{{ (random_integer / 2) | int }}</p>
<ul>
  {% for n in range(random_integer) %}
  {% if n % 2 %}
  <li>{{ n }}</li>
  {% endif %}
  {% endfor %}
</ul>
{% endblock %}
```

Ora è necessario generare tutti i file di traduzione e inserire le stringhe localizzate.

1. Collegarsi al container in esecuzione: `docker-compose -f docker-compose.yml -f docker-compose.dev.yml exec ckan bash`
2. Entrare nella cartella dell'estensione: `cd src_extensions/ckanext-estar/`
3. Generare il file `i18n/ckanext-estar.pot`: `python3 setup.py extract_messages` (l'estrazione dei messaggi viene effettuata in tutti i file indicati nella variabile `message_extractors` definita nel file `setup.py`)

```
#: ckanext/estar/templates/home/layout1.html:4
msgid "block header"
msgstr ""

#: ckanext/estar/templates/home/layout1.html:7
msgid "block footer"
msgstr ""
```

4. Inizializzare il catalogo per la lingua scelta: `python3 setup.py init_catalog -l it`
5. Tradurre le stringhe estratte nel nuovo file `ckanext-estar.po` nella cartella `i18n/it/LC_MESSAGES/` valorizzando le variabili `msgstr`

```
#: ckanext/estar/templates/home/layout1.html:4
msgid "block header"
msgstr "Intestazione del blocco"

#: ckanext/estar/templates/home/layout1.html:7
msgid "block footer"
msgstr "Piè di blocco"
```

6. Compilare il catalogo per la lingua scelta: `python3 setup.py compile_catalog` (viene creato/aggiornato il file `ckanext-estar.mo` nella cartella `i18n/it/LC_MESSAGES/`)
7. Ricaricare la homepage di CKAN

Per aggiungere la localizzazione in altre lingue è sufficiente ripetere il procedimento dal punto 4.

Con la stessa procedura è possibile sostituire le traduzioni originali di stringhe usate in CKAN, ma non necessariamente presenti nei template dell'estensione.

Per esempio si può modificare direttamente la traduzione della stringa `Welcome to CKAN` contenuta nel template `templates/home/snippets/promoted.html` (vedi [originale](https://github.com/ckan/ckan/blob/ckan-2.9.6/ckan/templates/home/snippets/promoted.html)) modificando il file `i18n/it/LC_MESSAGES/ckanext-estar.po`.

```
#: ckanext/estar/templates/home/layout1.html:4
msgid "block header"
msgstr "Intestazione del blocco"

#: ckanext/estar/templates/home/layout1.html:7
msgid "block footer"
msgstr "Piè di blocco"

#:
msgid "Welcome to CKAN"
msgstr "Benvenut* su ESTAR"
```

Man mano che si aggiungono stringhe di localizzazione:

1. estrarle nel file `pot`: `python3 setup.py extract_messages`
2. aggiornare i cataloghi (file `po`): `python3 setup.py update_catalog`
3. tradurre le stringhe nei file `po`
4. compilare le traduzioni (file `mo`): `python3 setup.py compile_catalog`

> ATTENZIONE: per modificarne i file all'interno della cartla `i18n/` è forse necessario modificarne opportunamente i permessi.

### Javascript personalizzato

Il codice javascript eseguito da CKAN è suddiviso in moduli indipendenti e un'estensione può registrare un nuovo modulo da fare eseguire in determinate pagine / circostanze.

Si rimanda alla [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/javascript.html) per tutti i dettagli.

## Laboratorio

Sviluppiamo un tema personalizzato.
