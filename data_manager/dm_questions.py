import connection
import uuid
import time
import util


def convert_query_to_dictionary(query):
    keys = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
    result = []
    for element in query:
        new_zip = zip(keys, element)
        new_dictionary = dict(new_zip)
        result.append(new_dictionary)
    print(result)
    return result


def get_all_questions_sql_sorted_by_submission_time():
    query = connection.connect_sql("""SELECT * FROM questions ORDER BY submission_time DESC;""")
    result = convert_query_to_dictionary(query)
    return result


def get_question_sql_by_id(id):
    query = connection.connect_sql(f"""SELECT * FROM questions WHERE id = '{id}'""")
    formatted_question = query
    result = convert_query_to_dictionary(formatted_question)
    return result[0]


def add_question_sql(data):
    id = uuid.uuid4()
    query = f"""INSERT INTO questions (id, vote_number, view_number, title, message) """ \
            f"""VALUES ('{id}', 0, 1, '{data['title']}', '{data['description']}');"""
    connection.connect_sql(query)


def update_question_sql(id, form_data):
    connection.connect_sql(f"""
                            UPDATE questions 
                            SET  title = '{form_data['title']}', message = '{form_data['description']}' 
                            WHERE id = '{id}'; 
                            """)


def get_questions_sorted(order_by, order_direction):
    query = connection.connect_sql(f"""SELECT * FROM questions ORDER BY {order_by} {order_direction};""")
    result = convert_query_to_dictionary(query)
    return result


def update_question_view_increase_count(id):
    connection.connect_sql(f"""UPDATE questions
                                    SET view_number = view_number + 1
                                    WHERE id = '{id}' """)



