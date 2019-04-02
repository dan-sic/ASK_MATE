from connection import connection_handler
from psycopg2 import sql
import datetime


@connection_handler
def get_all_questions_sql_sorted_by_submission_time(cursor):
    cursor.execute("""
                    SELECT * FROM question ORDER BY submission_time DESC
                    """)
    questions = cursor.fetchall()
    return questions


@connection_handler
def get_5_questions_sql_sorted_by_submission_time(cursor):
    cursor.execute("""
                    SELECT * FROM question ORDER BY submission_time DESC LIMIT 5
                    """)
    questions = cursor.fetchall()
    return questions


@connection_handler
def get_questions_sorted(cursor, order_by, order_direction):
    cursor.execute(f"""
                    SELECT * FROM question ORDER BY {order_by} {order_direction}
                    """)
    questions = cursor.fetchall()
    return questions


@connection_handler
def get_question_sql_by_id(cursor, id):
    cursor.execute(f'SELECT * FROM question WHERE id={id}')
    question = cursor.fetchall()
    return question


@connection_handler
def add_question_sql(cursor, form_data):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # to check > why we need extra quotes around expressions?
    #  to check > how to process this with sql.SQL?
    #  to check > how to validate user input?
    # to check > should we only validate input from direct user input, or also URL strings?
    cursor.execute(f"""
                    INSERT INTO question (submission_time, view_number, vote_number, title, message) \
                    VALUES ('{time}', 0, 0, '{form_data['title']}', '{form_data['message']}')
                    """)


@connection_handler
def update_question_sql(cursor, id, form_data):
    cursor.execute(f"""
                    UPDATE question
                    SET  title = '{form_data['title']}', message = '{form_data['message']}' 
                    WHERE id = '{id}'
                    """)


@connection_handler
def update_question_view_increase_count(cursor, id):
    cursor.execute(f"""
                    UPDATE question
                    SET view_number = view_number + 1
                    WHERE id = '{id}'
                    """)

