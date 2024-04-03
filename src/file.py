import json
import os
from utils import to_date, remove_duplicate


def get_filepath():
    # get json file
    dir = os.getcwd()
    return os.path.join(dir, "data", "news.json")

def load_from_json(filepath):
    data = []
    try:
        # load existing data
        with open(filepath, 'r') as file:
            data = json.loads(file.read())
            file.close()
        return data
    except IOError:
        print("[WARN] Failed to load existing data.")

def transform_data(data: list, filepath) -> list:
    # load existing data
    existing_data = load_from_json(filepath)
    if existing_data:
        data.extend(existing_data)
    # sort from latest (descending) by date scrapped
    data = sorted(data, reverse=True, key=lambda d: to_date(d["waktu_scraping"]))
    # remove duplicate
    data = remove_duplicate(data, "judul")
    
    return data

def write_file(data, filepath):
    # write to files
    print("[INFO] saving headline news to data/news.json ...")
    try:
        with open(filepath, 'w') as file:
            file.writelines(data)
            file.close()
        print("[INFO] Success saving data to file.")
    except IOError:
        print("[WARN] Failed to save data.")

def save_to_json(data: list, filepath):
    # cleaning data
    data = transform_data(data, filepath)
    # convert list of dictionaries to json objects
    jdumps = json.dumps(data)
    # save data to file
    write_file(jdumps, filepath)
