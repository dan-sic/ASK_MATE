import connection
import uuid
import time
import util
import os


def convert_query_to_dictionary(query):
    keys = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
    result = []
    for element in query:
        new_zip = zip(keys, element)
        new_dictionary = dict(new_zip)
        result.append(new_dictionary)
    print(result)
    return result


def get_all_sql_answers():
    query = connection.connect_sql("""SELECT * FROM answers""")
    results = convert_query_to_dictionary(query)
    return results


def get_all_sql_answers_by_question_id(id):
    query = connection.connect_sql(f"""SELECT * FROM answers WHERE question_id = '{id}' """)
    print(id)
    results = convert_query_to_dictionary(query)
    print('to są wynii',results)
    return results


def add_sql_answer(form_data, question_id):
    id = uuid.uuid4()
    print('dione?')
    query = (f"""INSERT INTO answers (id, vote_number, question_id, message)
                            VALUES ('{id}', 0, '{question_id}', '{form_data['answer']}') """)
    connection.connect_sql(query)
