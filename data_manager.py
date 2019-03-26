import connection


def get_all_questions():
    q_list = sorted(connection.read_file(), key=lambda k: k['submission_time'], reverse=True)
    return q_list


def save_new_question(record):
    connection.write_file(record, 'questions.csv')


def get_question_by_id(id):
    q_list = connection.read_file('questions.csv')
    for element in q_list:
        if element['id'] == id:
            return element
