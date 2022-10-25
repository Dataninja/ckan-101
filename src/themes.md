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

La [documentazione ufficiale](https://docs.ckan.org/en/2.9/theming/index.html) è molto ampia e approfondita,
nella [sezione sulle estensioni](./extensions#sviluppo-di-un-estensione) sono riportati i principali passaggi per inizializzare un'estensione vuota su cui lavorare in modalità sviluppo.

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

Sviluppiamo un tema personalizzato.
