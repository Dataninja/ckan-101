import os, json
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry
from geoalchemy2.functions import ST_GeomFromGeoJSON

db_string = f"postgresql://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', 'postgres')}@{os.getenv('DB_HOST', 'localhost')}:5432/{os.getenv('DB_NAME', 'postgres')}"

base = declarative_base()


class Region(base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    geom = Column(Geometry('MULTIPOLYGON'))

db = create_engine(db_string)
Session = sessionmaker(db)
session = Session()

if __name__ == "__main__":

    with open("regions.geojson") as f:
      regions = json.load(f)

    base.metadata.create_all(db)

    # Create
    for region in regions["features"]:
        session.add(
            Region(
                id=region["properties"]["reg_istat_code_num"],
                name=region["properties"]["reg_name"],
                geom=ST_GeomFromGeoJSON(json.dumps(region["geometry"]))
            )
        )

    session.commit()
