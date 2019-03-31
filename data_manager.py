import connection
import uuid
import time
import util
import os


def get_all_questions():
    questions = connection.read_file()
    sorted_questions = sorted(questions, key=lambda k: k['submission_time'], reverse=True)
    questions_with_proper_date_format = map(util.convert_time_value_to_formatted_string, sorted_questions)
    return questions_with_proper_date_format


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


def get_question_by_id(id):
    questions = connection.read_file()
    for question in questions:
        if question['id'] == id:
            formatted_question = util.convert_time_value_to_formatted_string(question)
            return formatted_question


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


def question_view_count_increase(id):
    questions = connection.read_file()
    for question in questions:
        if question['id'] == id:
            question['view_number'] = str(int(question['view_number']) + 1)
    connection.write_file(questions)


def update_question(id, form_data):
    questions = connection.read_file()
    for question in questions:
        if question['id'] == id:
            question['title'] = form_data['title']
            question['message'] = form_data['description']
    connection.write_file(questions)


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


def delete_element(element_type, element_id):

    # delete file if exists
    data = connection.read_file(f'{element_type}.csv')
    try:
        deleted_element_img_path = [element['image'] for element in data if element['id'] == element_id][0]
        file_name = deleted_element_img_path.split("/")[1]
        if file_name:
            os.remove(f"static/images/{file_name}")
    except IndexError:
        pass

    # delete element
    updated_data = [data_element for data_element in data if data_element['id'] != element_id]
    connection.write_file(updated_data, f'{element_type}.csv')

    # if question is deleted - also delete corresponding answers
    if element_type == "questions":
        answers = connection.read_file('answers.csv')

        # delete answer's image
        img_paths_of_deleted_answers = [answer['image'] for answer in answers if answer['question_id'] == element_id]
        for img_path in img_paths_of_deleted_answers:
            try:
                file_name = img_path.split("/")[1]
                if file_name:
                    os.remove(f"static/images/{file_name}")
            except IndexError:
                pass
            
        # delete answer
        updated_answers = [answer for answer in answers if answer['question_id'] != element_id]
        connection.write_file(updated_answers, 'answers.csv')


def sort_questions(order_by, order_direction):
    questions = connection.read_file()
    sort_type = True if order_direction == 'asc' else False
    sorted_questions = sorted(questions, key=lambda k: k[order_by], reverse=sort_type)
    questions_with_proper_date_format = map(util.convert_time_value_to_formatted_string, sorted_questions)
    return questions_with_proper_date_format


def update_image(file_type, filename, id):
    data = connection.read_file(f"{file_type}.csv")
    for element in data:
        if element['id'] == id:
            element['image'] = 'images/' + filename
    connection.write_file(data, f"{file_type}.csv")


def change_vote(file_type, id, change_step):
    data = connection.read_file(f"{file_type}.csv")
    for element in data:
        if element['id'] == id:
            element['vote_number'] = str(int(element['vote_number']) + change_step)
    connection.write_file(data, f"{file_type}.csv")


def add_question_sql(data):
    id = uuid.uuid4()
    query = f"INSERT INTO questions (id, vote_number, view_number, title, message) " \
            f"VALUES ('{id}', 0, 1, '{data['title']}', '{data['description']}');"
    connection.connect_sql(query)




