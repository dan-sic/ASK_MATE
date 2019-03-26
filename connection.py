import csv


def read_file(filename="data/questions.csv"):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data


def write_file(dict_list, filename="questions.csv"):
    keys = dict_list[0].keys()
    filedirectory = 'data/' + filename
    with open(filedirectory, 'w') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(dict_list)
