from connection import connection_handler
import os


@connection_handler
def update_image_path(cursor, table, filename, id):
    cursor.execute(f"""
                    UPDATE {table} 
                    SET image = 'images/{filename}' WHERE id={id}
                    """)


@connection_handler
def remove_image(cursor, table, id):
    file_path = cursor.execute(
        # todo > check why file_path is returning None even though question has image path
        # todo > check why  query does not work without f strings
        # "select image from %(table)s where id=%(id)s", {"table": table, "id": id}
        # sql.SQL("select image from {table} WHERE id={id}").format(table=sql.Identifier(table), id=sql.Identifier(id))
        f"SELECT image FROM {table} WHERE id={id}"
    )
    if file_path:
        # todo > check if it will work with url_for()
        # os.remove(f"static/{file_path}")f"static/{file_path}"
        os.remove(f"../static/{file_path}")


@connection_handler
def search_results(cursor, search_term):

    cursor.execute("""
            SELECT DISTINCT q.* FROM question q JOIN answer a ON q.id=a.question_id WHERE
            UPPER(q.title) LIKE UPPER(%(search_term)s)
            OR UPPER(q.message) LIKE UPPER(%(search_term)s)
            OR UPPER(a.message) LIKE UPPER(%(search_term)s);
                    """, {'search_term': '%'+search_term+'%'})
    questions = cursor.fetchall()
    cursor.execute("""
            SELECT * FROM answer WHERE UPPER(message) LIKE UPPER(%(search_term)s)
                    """, {'search_term': '%'+search_term+'%'})
    answers = cursor.fetchall()
    return questions, answers
