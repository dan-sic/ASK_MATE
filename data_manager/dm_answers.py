from connection import connection_handler
import datetime
import util
import os
from data_manager import dm_general


@connection_handler
def get_all_sql_answers_by_question_id(cursor, question_id):
    cursor.execute("""
                    SELECT * FROM answer WHERE question_id=%(question_id)s
                    """,
                    {"question_id": question_id})
    answers = cursor.fetchall()
    return answers


@connection_handler
def qet_answer_by_id(cursor, answer_id):
    cursor.execute("""
                    SELECT * FROM answer WHERE id=%(answer_id)s
                    """,
                    {"answer_id": answer_id})
    answer_in_list = cursor.fetchall()
    if answer_in_list:
        return answer_in_list[0]
    else:
        return None



@connection_handler
def add_sql_answer(cursor, form_data, question_id):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(f"""
                    INSERT INTO answer (submission_time, vote_number, question_id, message) \
                    VALUES ('{time}', 0, '{question_id}', '{form_data['answer']}')
                    """)


@connection_handler
def delete_answer(cursor, id):
    # delete answer image if exists
    dm_general.remove_image('answer', id)

    # delete answer and all related comments
    cursor.execute(
                f"""
            DELETE FROM comment WHERE answer_id={id};
            DELETE FROM answer WHERE id={id};
                """
            )

@connection_handler
def update_answer(cursor, answer_id, form_data):
    cursor.execute(
        """
            UPDATE answer SET message=%(answer)s WHERE id=%(answer_id)s
        """, {"answer": form_data['answer'], "answer_id": answer_id}
    )
