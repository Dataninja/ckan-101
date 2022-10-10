import os
from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = f"postgresql://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', 'postgres')}@{os.getenv('DB_HOST', 'localhost')}:5432/{os.getenv('DB_NAME', 'postgres')}"

base = declarative_base()


class Page(base):
    __tablename__ = 'pages'

    slug = Column(String, primary_key=True)
    title = Column(String)
    content = Column(String)


db = create_engine(db_string)
Session = sessionmaker(db)
session = Session()

if __name__ == "__main__":

    pages = {
        "welcome": "Questo corso copre le basi di CKAN (uso, amministrazione e sviluppo) ed è rivolto primariamente a sviluppatori e amministratori di sistema.",
        "introduction": "CKAN si definisce un Data Management System (DMS), un’applicazione specializzata che ricade nella più vasta categoria di Content Management System (CMS) resa popolare da Wordpress.",
        "overview": "CKAN è un software monolitico, ma con una struttura modulare del codice."
    }

    base.metadata.create_all(db)

    # Create
    for page in pages:
        session.add(
            Page(
                slug=page,
                title=page.title(),
                content=pages[page]
            )
        )

    session.commit()
