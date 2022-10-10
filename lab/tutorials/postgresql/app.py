from flask import Flask, render_template
from datetime import datetime
from db import session, Page

app = Flask(__name__)


@app.route('/')
def index():
    pages = session.query(Page)
    data = {
        "title": "CKAN 101",
        "pages": [page.slug for page in pages],
        "datetime": datetime.now()
    }
    return render_template("home.html", **data)


@app.route('/<slug>')
def page(slug):
    page = session.query(Page).get(slug)
    data = {
        "title": page.title if page else slug.title(),
        "content": page.content if page else "No content...",
        "datetime": datetime.now()
    }
    return render_template("page.html", **data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
