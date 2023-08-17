import json
import GLOBAL as G


def read_data(file_path: str):
    try:
        with open(file_path, 'r') as file:
            data_file = file.read()
            data_dict = json.loads(data_file)
            if len(data_dict) == 0:
                return G.EMPTY
            return data_dict
    except Exception as e:
        print(e)
        return G.EMPTY


def append_data(new_data: dict, filepath: str):
    try:
        all_data = read_data(filepath)  # list of dicts
        if all_data == G.EMPTY:
            all_data = list()
        with open(filepath, 'w') as file:
            all_data.append(new_data)
            data = json.dumps(all_data, indent=4)  # convert list of dicts to string
            file.write(data)  # write data to the file ?
    except Exception as e:
        print(e)


def write_data(new_data: dict, filepath: str):
    try:
        with open(filepath, 'w') as file:
            data = json.dumps(new_data, indent=4)  # convert list of dicts to string
            file.write(data)  # write data to the file ?
    except Exception as e:
        print(e)
