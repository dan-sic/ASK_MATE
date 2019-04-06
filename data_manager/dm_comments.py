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
def add_comment_to_answer(cursor, form_data, answer_id):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(f"""
                    INSERT INTO comment
                    (edited_count, message, answer_id, submission_time)
                    VALUES (0, '{form_data['message']}', '{answer_id}', '{time}')
""")


@connection_handler
def show_question_comments_by_id(cursor, id):
    cursor.execute(f"""
                    SELECT * FROM comment
                    WHERE question_id = {id};
""")
    comments = cursor.fetchall()
    return comments


@connection_handler
def show_answer_comments_by_id(cursor, id):
    cursor.execute(f"""
                    SELECT * FROM comment
                    WHERE answer_id = {id};  
""")
    comments = cursor.fetchall()
    return comments
