import json


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)




