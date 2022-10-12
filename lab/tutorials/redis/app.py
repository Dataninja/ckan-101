import os, requests
from random import shuffle
from flask import Flask, render_template
from datetime import datetime
from db import session, Region
from geoalchemy2.functions import ST_MakePoint, ST_SetSRID
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_URL": f"redis://{os.getenv('REDIS_HOST', 'localhost')}:6379/0"
})


cities = [
    "Aosta", "Torino", "Genova", "Milano", "Trento", "Venezia", "Trieste", "Bologna", "Firenze", "Ancona", "Perugia", "Roma", "L'Aquila", "Campobasso", "Napoli", "Bari", "Potenza", "Catanzaro", "Palermo", "Cagliari",
    "Arezzo", "Grosseto", "Livorno", "Lucca", "Massa-Carrara", "Pisa", "Pistoia", "Prato", "Siena"
]

shuffle(cities)

@app.route('/')
def index():
    data = {
        "name": "CKAN 101",
        "pages": [city.lower() for city in cities],
        "datetime": datetime.now()
    }
    return render_template("home.html", **data)


@app.route('/<slug>')
@cache.cached(timeout=300)
def page(slug):
    r = requests.get(f"https://nominatim.openstreetmap.org/search?city={slug}&format=json").json()
    city = r[0] if r else {}
    point = ST_SetSRID(ST_MakePoint(float(city["lon"]), float(city["lat"])), 4326)
    regions = session.query(Region).filter(Region.geom.ST_Contains(point)) if city else []
    data = {
        "name": slug.title(),
        "region": regions[0].name if regions else "sconosciuta",
        "datetime": datetime.now()
    }
    return render_template("page.html", **data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
