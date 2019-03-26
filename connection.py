import csv


def read_file(filename="questions.csv"):
    file_directory = 'data/' + filename
    with open(file_directory, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data


def write_file(dict_list, filename="questions.csv"):
    keys = dict_list[0].keys()
    file_directory = 'data/' + filename
    with open(file_directory, 'w') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(dict_list)
