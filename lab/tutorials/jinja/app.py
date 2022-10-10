from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

pages = {
  "welcome": "Questo corso copre le basi di CKAN (uso, amministrazione e sviluppo) ed è rivolto primariamente a sviluppatori e amministratori di sistema.",
  "introduction": "CKAN si definisce un Data Management System (DMS), un’applicazione specializzata che ricade nella più vasta categoria di Content Management System (CMS) resa popolare da Wordpress.",
  "overview": "CKAN è un software monolitico, ma con una struttura modulare del codice."
}


@app.route('/')
def index():
    data = {
        "title": "CKAN 101",
        "pages": pages.keys(),
        "datetime": datetime.now()
    }
    return render_template("home.html", **data)

@app.route('/<slug>')
def page(slug):
    data = {
        "title": slug.title(),
        "content": pages.get(slug, "No content..."),
        "datetime": datetime.now()
    }
    return render_template("page.html", **data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
