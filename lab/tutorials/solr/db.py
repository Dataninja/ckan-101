import os, pysolr, nltk

solr = pysolr.Solr(f"http://{os.getenv('SOLR_HOST', 'localhost')}:8983/solr/gettingstarted/", always_commit=True)

nltk.download('reuters')


if __name__ == "__main__":

    solr.add([
      {
        "id": take_id,
        "take_txt_en": nltk.corpus.reuters.raw(take_id)
      }
      for take_id in nltk.corpus.reuters.fileids()
    ])

    print(f"{len(nltk.corpus.reuters.fileids())} takes indexed")
