import requests
from datetime import datetime, date, timedelta
from elasticsearch import Elasticsearch
import warnings
import pandas
import file_utils

warnings.filterwarnings("ignore", category=DeprecationWarning)

es_hosts = "http://localhost:9200"
es_index = "imdb_movies"


def save_elasticsearch_es(index, es_data):
    es = Elasticsearch(hosts=es_hosts)
    es.update(index=index, id=es_data['imdb_title_id'], body={'doc': es_data, 'doc_as_upsert': True})


def es_preprocess_index(index):
    es = Elasticsearch(hosts=es_hosts)  # Your auth data

    # Define the index settings and mappings (optional)
    mappings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
                "timestamp": {"type": "date"},
                "imdb_title_id": {"type": "keyword"},
                "title": {"type": "keyword"},
                "date_publish": {"type": "date"},
                "country": {"type": "keyword"},
                "avg_vote": {"type": "float"},
                "votes": {"type": "integer"},
                "budget": {"type": "float"},
                "usa_gross_income": {"type": "float"},
                "worlwide_gross_income": {"type": "float"},
                "reviews_from_users": {"type": "integer"}
            }
        }
    }

    # Create the new index
    es.indices.create(index=index,
                      mappings=mappings,
                      ignore=400  # ignore 400 already exists code
                      )
def main():
    # es_preprocess_index(es_index)
    # csv_file = "IMDB Movies 2000 - 2020.csv"
    json_file = "IMDB Movies 2000 - 2020.json"
    # csv_to_json.convert_csv_to_json(csv_file, json_file)

    imdb_movies = file_utils.read_json_data(json_file)
    es_collections = []
    for movie in imdb_movies:
        timestamp = datetime.strptime(movie['date_published'], '%d/%m/%Y').isoformat()
        es_docs = {
            "timestamp": timestamp,
            "imdb_title_id": movie['imdb_title_id'],
            "title": movie['title'],
            "date_publish": movie['date_published'],
            "country": movie['country'],
            "avg_vote": movie['avg_vote'],
            "votes": movie['votes'],
            "budget": movie['budget'],
            "usa_gross_income": movie['usa_gross_income'],
            "worlwide_gross_income": movie['worlwide_gross_income'],
            "reviews_from_users": movie['reviews_from_users']
        }
        # es_collections.append(es_docs)
        save_elasticsearch_es(es_index, es_docs)

    print(imdb_movies)

if __name__ == "__main__":
    main()
