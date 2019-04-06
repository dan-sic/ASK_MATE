from connection import connection_handler
import datetime


@connection_handler
def add_comment_to_question(cursor, form_data, question_id):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(f"""
                    INSERT INTO comment
                    (edited_count, message, question_id, submission_time)
                    VALUES (0, '{form_data['message']}', '{question_id}', '{time}')
""")


@connection_handler
def add_comment_to_answer(cursor, form_data, answer_id, question_data):
    question_id = question_data['question_id']
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(f"""
                    INSERT INTO comment
                    (edited_count, message, answer_id, submission_time, question_id)
                    VALUES (0, '{form_data['message']}', '{answer_id}', '{time}', '{question_id}')
""")


@connection_handler
def show_question_comments_by_id(cursor, id):
    cursor.execute(f"""
                    SELECT * FROM comment
                    WHERE question_id = '{id}';
""")
    comments = cursor.fetchall()
    return comments


@connection_handler
def show_answer_comments_by_id(cursor, id):
    cursor.execute(f"""
                    SELECT * FROM comment
                    WHERE answer_id = '{id}';  
""")
    comments = cursor.fetchall()
    return comments


@connection_handler
def get_comment_by_id(cursor, id):
    cursor.execute(f"""
                    SELECT * FROM comment
                    WHERE id = '{id}';
""")
    comment = cursor.fetchall()
    return comment


@connection_handler
def update_comment_by_id(cursor, form_data, id):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(f"""
                    UPDATE comment
                    SET message = '{form_data['message']}', edited_count = edited_count + 1, submission_time = '{time}'
                    WHERE id = '{id}'; 
                    SELECT question_id, answer_id FROM comment
                    WHERE id = '{id}'
""")
    question_id = cursor.fetchall()
    return question_id

