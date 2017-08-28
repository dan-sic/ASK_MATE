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


def sort_questions(order_by, order_direction):
    questions = connection.read_file()
    sort_type = True if order_direction == 'asc' else False
    sorted_questions = sorted(questions, key=lambda k: k[order_by], reverse=sort_type)
    questions_with_proper_date_format = map(util.convert_time_value_to_formatted_string, sorted_questions)
    return questions_with_proper_date_format


def question_view_count_increase(id):
    questions = connection.read_file()
    for question in questions:
        if question['id'] == id:
            question['view_number'] = str(int(question['view_number']) + 1)
    connection.write_file(questions)


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