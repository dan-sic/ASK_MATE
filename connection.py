import csv


def read_file(filename="questions.csv"):
    file_directory = 'data/' + filename
    with open(file_directory, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data


def write_file(dict_list, filename="questions.csv"):
    keys = ["id", "submission_time", "view_number", "vote_number", "title", "message", "image"]
    if filename == 'answers.csv':
        keys = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    file_directory = 'data/' + filename
    with open(file_directory, 'w') as f:
        writer = csv.DictWriter(f, keys)
        writer.writeheader()
        writer.writerows(dict_list)
