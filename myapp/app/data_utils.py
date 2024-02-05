import csv
import json

def read_csv_to_dicts(filename):
    """Reads a CSV file and returns the data as a list of dictionaries.

    Args:
        filename (str): The name of the CSV file to read.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the CSV file.
    """

    with open(filename, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    return data

def convert_to_json(data):
    """Converts a list of dictionaries to a JSON string.

    Args:
        data (list): A list of dictionaries to convert.

    Returns:
        str: A JSON string representation of the data.
    """

    json_data = json.dumps(data, indent=2)  # Adds indentation for readability
    return json_data

# Example usage
# data = read_csv_to_dicts("test-data.csv")
# json_string = convert_to_json(data)
# print(json_string)

# import pprint
# data=read_csv_to_dicts("test-data.csv")
# pprint.pprint(d)
