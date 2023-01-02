import csv
import json


def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


def write_json_file(json_file_path, data):
    with open(json_file_path, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    data = read_csv('./data.csv')
    print[data[0]]
    write_json_file('./data.json', data)
