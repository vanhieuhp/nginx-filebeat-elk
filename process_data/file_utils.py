import csv
import json

def convert_csv_to_json(input, output):
    with open(input, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    with open(output, 'w') as jsonfile:
        json.dump(data, jsonfile)

def read_json_data(input):

    with open(input) as file:
        data = json.load(file)
        return data
