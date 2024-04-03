import json
import os


def get_filepath():
    # get json file
    dir = os.getcwd()
    return os.path.join(dir, "data", "news.json")

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
    # convert list of dictionaries to json objects
    jdumps = json.dumps(data)
    # save data to file
    write_file(jdumps, filepath)
