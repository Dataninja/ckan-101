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

Esempio per nascondere l'immagine in homepage nella card di benvenuto: `.homepage .featured .media-image { display: none; }`.

## Temi di terze parti

Un tema di CKAN è un'estensione, quindi se rilasciata in open source si può scaricare e installare (vedi la [sezione sulle estensioni](./extensions)). È molto difficile però scrivere un tema personalizzabile e abbastanza flessibile da essere riutilizzato, quindi se ne trovano molto pochi.

## Sviluppo di un tema

...

### Template di pagina personalizzati

...

### CSS personalizzato

...

### Immagini personalizzate

...

### Traduzioni personalizzate

...

### Javascript personalizzato

...

## Laboratorio

...
