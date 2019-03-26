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


def get_all_answers():
    a_list = connection.read_file('answers.csv')
    return a_list


def get_answers_by_question_id(id):
    a_list = connection.read_file('answers.csv')
    new_a_list = []
    for element in a_list:
        if element['question_id'] == id:
            new_a_list.append(element)
    return new_a_list


def save_new_answer(record):
    connection.write_file(record, 'answers.csv')
