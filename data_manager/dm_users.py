from connection import connection_handler


@connection_handler
def get_users(cursor):
    cursor.execute("""
                    SELECT * FROM users
                    """)
    users = cursor.fetchall()
    return users


@connection_handler
def get_user(cursor, user_id):
    cursor.execute("""
                    SELECT * FROM users
                    WHERE id=%(id)s
                    """,
                   {'id': user_id})
    user = cursor.fetchone()
    return user


@connection_handler
def get_user_questions(cursor, user_id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE users_id=%(id)s
                    """,
                   {'id': user_id})
    questions = cursor.fetchall()
    return questions, len(questions)


@connection_handler
def get_user_answers_wth_corresponding_question_titles(cursor, user_id):
    cursor.execute("""
                    SELECT answer.*, question.title as question_title
                    FROM answer LEFT JOIN question
                    ON answer.question_id=question.id
                    WHERE answer.users_id=%(id)s
                    """,
                   {'id': user_id})
    answers = cursor.fetchall()
    return answers, len(answers)


@connection_handler
def get_user_comments_with_corresponding_question(cursor, user_id):
    cursor.execute("""
                    SELECT comment.*, question.title as question_title
                    FROM comment LEFT JOIN question
                    ON comment.question_id=question.id
                    WHERE comment.users_id=%(id)s
                    """,
                   {'id': user_id})
    comments = cursor.fetchall()
    return comments, len(comments)


@connection_handler
def get_users_sorted(cursor, order_by, order_direction):
    cursor.execute(f"""
                    SELECT * FROM users ORDER BY {order_by} {order_direction}
                    """)
    users = cursor.fetchall()
    return users


@connection_handler
def update_user_reputation(cursor, users_id, value):
    print(users_id, value)
    cursor.execute("""
                    UPDATE users
                    SET  reputation = reputation + %(reputation)s
                    WHERE id = %(users_id)s
                    """,
                   {'reputation': value, 'users_id': users_id})
