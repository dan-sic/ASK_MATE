import connection
import uuid
import time
import util
import os


def get_all_answers():
    a_list = connection.read_file('answers.csv')
    return a_list


def get_answers_by_question_id(id):
    answers = connection.read_file('answers.csv')
    answers_to_question = []
    for answer in answers:
        if answer['question_id'] == id:
            answer_with_proper_date_format = util.convert_time_value_to_formatted_string(answer)
            answers_to_question.append(answer_with_proper_date_format)
    return answers_to_question


def add_answer(form_data, id):
    answers = connection.read_file('answers.csv')
    new_answer = {
        'id': uuid.uuid4(),
        'submission_time': time.time(),
        'vote_number': 0,
        'question_id': id,
        'message': form_data['answer'],
        'image': None
    }
    answers.append(new_answer)
    connection.write_file(answers, 'answers.csv')
