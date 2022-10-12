from flask import Flask, request, render_template
from datetime import datetime
from db import solr

app = Flask(__name__)


@app.route('/')
def index():
    data = {
        "title": "CKAN 101",
        "datetime": datetime.now()
    }
    return render_template("home.html", **data)


@app.route('/search')
def search():
    q = request.args.get("q") or "*"
    return list(solr.search(f"take_txt_en:{q}"))


@app.route('/similar')
def similar():
    id = request.args.get("id")
    documents = list(solr.search(f"id:{id}"))
    data = {
      "title": id or "Not found",
      "content": documents[0]["take_txt_en"] if documents else "",
      "documents": list(solr.more_like_this(q=f"id:{id}", mltfl='take_txt_en')) if id else []
    }
    return render_template("page.html", **data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
