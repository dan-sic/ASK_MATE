from connection import connection_handler
import datetime


@connection_handler
def add_comment_to_question(cursor, form_data, question_id):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('itssds', form_data)
    cursor.execute(f"""
                    INSERT INTO comment
                    (edited_count, message, question_id, submission_time)
                    VALUES (0, '{form_data['message']}', '{question_id}', '{time}')
""")


@connection_handler
def show_question_comments_by_id(cursor, id):
    cursor.execute(f"""
                    SELECT * FROM comment
                    WHERE id = {id}
""")
    comments = cursor.fetchall()
    return comments