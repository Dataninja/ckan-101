from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

diagram_attr = { "margin": "-2, -2" }

with Diagram(
  "CKAN Entities schema\nCC0 - Public domain",
  graph_attr=diagram_attr,
  filename="entities",
  show=False,
  direction="TB"
):

  # Thanks to https://boykoc.github.io/ckan/2019/10/21/ckan-283-database-diagram.html
  activity = Custom("Activity", "icons/activity.png") # User activities in CKAN related to an object.
  topic = Custom("Topic", "icons/topic.png") # Represents simple way to manage collections of packages by topic.
  organization = Custom("Organization", "icons/organization.png") # Represents simple way to manage collections of packages by topic.
  dataset = Custom("Dataset / Package", "icons/dataset.png") # Represents the dataset and related metadata.
  tag = Custom("Tag", "icons/tag.png") # Represents the tags for packages which are used to group/classify datasets, associates tags to packages.
  rating = Custom("Rating", "icons/rating.png") # User rating of a dataset (package).
  resource = Custom("Resource", "icons/resource.png") # Represents the structure data files and technical documents related to a package (dataset).
  user = Custom("User", "icons/user.png") # Represents a list of users in the system.
  vocabulary = Custom("Vocabulary", "icons/vocabulary.png") # Tag vocabulary are a way of grouping related tags together into custom fields.

  activity - user
  rating - user

  user - organization

  dataset - organization
  dataset - topic
  dataset - user
  dataset - tag
  dataset - rating
  dataset - resource

  tag - vocabulary
