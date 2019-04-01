import connection
import uuid
import time
import util


def add_question(form_data):
    questions = connection.read_file()
    new_question = {
        'id': uuid.uuid4(),
        'title': form_data['title'],
        'message': form_data['description'],
        'submission_time': time.time(),
        'view_number': 0,
        'vote_number': 0,
        'image': None
    }
    questions.append(new_question)
    connection.write_file(questions, 'questions.csv')


def get_all_questions():
    questions = connection.read_file()
    sorted_questions = sorted(questions, key=lambda k: k['submission_time'], reverse=True)
    questions_with_proper_date_format = map(util.convert_time_value_to_formatted_string, sorted_questions)
    return questions_with_proper_date_format


def get_question_by_id(id):
    questions = connection.read_file()
    for question in questions:
        if question['id'] == id:
            formatted_question = util.convert_time_value_to_formatted_string(question)
            return formatted_question


def update_question(id, form_data):
    questions = connection.read_file()
    for question in questions:
        if question['id'] == id:
            question['title'] = form_data['title']
            question['message'] = form_data['description']
    connection.write_file(questions)