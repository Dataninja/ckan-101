from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import Postgresql
from diagrams.onprem.search import Solr
from diagrams.onprem.inmemory import Redis
from diagrams.custom import Custom

diagram_attr = { "margin": "-2, -2" }
cluster_attr = { "margin": "10, 10" }

with Diagram(
  "CKAN Services schema\nCC0 - Public domain",
  graph_attr=diagram_attr,
  filename="services",
  show=False,
  direction="TB"
):

    with Cluster("Cache database", graph_attr=cluster_attr):

      cache_database = Redis("Redis")

    with Cluster("Main database", graph_attr=cluster_attr):

      main_database = Postgresql("PostgreSQL")
      main_database_volume = Custom("pg_data", "icons/volume.png")

    with Cluster("Search engine", graph_attr=cluster_attr):

      search_engine = Solr("Solr")
      search_engine_volume = Custom("solr_data", "icons/volume.png")

    with Cluster("CKAN", graph_attr=cluster_attr):

      ckan_core = Custom("", "icons/ckan.png")
      ckan_datapusher = Custom("Datapusher", "icons/datapusher.png")

      ckan_config_volume = Custom("ckan_config", "icons/volume.png")
      ckan_home_volume = Custom("ckan_home", "icons/volume.png")
      ckan_storage_volume = Custom("ckan_storage", "icons/volume.png")

    ckan_core >> Edge(color = "#336791") << main_database
    ckan_core >> Edge(color = "#c7402b") << search_engine
    ckan_core >> Edge(color = "#d82c20") << cache_database
    ckan_core >> Edge(color = "#f03b41") << ckan_datapusher

    main_database - Edge(style="dashed") - main_database_volume
    search_engine - Edge(style="dashed") - search_engine_volume
    ckan_core - Edge(style="dashed") - ckan_config_volume
    ckan_core - Edge(style="dashed") - ckan_home_volume
    ckan_core - Edge(style="dashed") - ckan_storage_volume
