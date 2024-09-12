import requests
from datetime import datetime, date, timedelta
from elasticsearch import Elasticsearch
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

es_hosts = "http://localhost:9200"

def get_list_states():
    url = "https://api.covidtracking.com/v2/states.json"
    r = requests.get(url)
    data = r.json()
    result = []
    for state in data['data']:
        result.append({"state_name": state['name'], "state_code": state['state_code']})

    return result

def save_elasticsearch_es(index, es_data):
    es = Elasticsearch(hosts=es_hosts)

    id_case = str(es_data['timestamp'].strftime("%d-%m-%Y")) + '-'+ es_data['state_name']
    es.update(index=index, id=id_case, body={'doc':es_data,'doc_as_upsert':True})

def es_preprocess_index(index):
    es = Elasticsearch(hosts=es_hosts) #Your auth data

    # Define the index settings and mappings (optional)
    mappings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
                "timestamp": {"type": "date"},
                "state_name": {"type": "keyword"},
                "total_diseases": {"type": "integer"},
                "infection_rate": {"type": "float"}
            }
        }
    }

    # Create the new index
    es.indices.create(index=index,
                      mappings=mappings,
                      ignore=400 # ignore 400 already exists code
    )

def fetch_data_all_states_daily(es_index, states, day):
    for state in states:
        url = f"https://api.covidtracking.com/v2/states/{state.get('state_code')}/{day}.json".lower()
        response = requests.get(url)
        json_data = response.json()

        total_diseases = json_data["data"]["cases"]["total"]["value"]
        infection_rate = json_data["data"]["cases"]["total"]["calculated"]["population_percent"]
        timestamp = datetime.strptime(day, "%Y-%m-%d")
        state_name = state["state_name"]

        es_data = {
            "timestamp": timestamp,
            "state_name": state_name,
            "total_diseases": total_diseases,
            "infection_rate": infection_rate
        }
        save_elasticsearch_es(es_index, es_data)



def main():
    es_index = "covid-19-live-global"
    es_preprocess_index(es_index)

    start_date = date(2020, 4, 1)
    end_date = date(2020, 4, 4)
    delta = timedelta(days=1)
    day = start_date.strftime("%Y-%m-%d")
    states = get_list_states()

    while start_date <= end_date:
        fetch_data_all_states_daily(es_index, states, day)
        start_date += delta
        day = start_date.strftime("%Y-%m-%d")


if __name__ == "__main__":
    main()