from connection import connection_handler


@connection_handler
def get_tags_of_question_by_id(cursor, id):
    int_id = int(id)
    cursor.execute(f"""
                    SELECT DISTINCT *
                        FROM question_tag INNER JOIN tag
                            ON question_tag.tag_id = tag.id
                    WHERE question_tag.question_id = {int_id};
""")
    tags = cursor.fetchall()
    return tags


@connection_handler
def get_all_tags(cursor):
    cursor.execute("""
                    SELECT DISTINCT * FROM tag 
                    ORDER BY name ASC;
""")
    tags = cursor.fetchall()
    return tags


@connection_handler
def add_tag_to_question(cursor, id, tag_id):
    cursor.execute(f"""
                    INSERT INTO question_tag (question_id, tag_id)
                    VALUES ({id}, {tag_id})
""")


@connection_handler
def get_tag_id_by_tag_name(cursor, tag_name):
    if tag_name['tag'] != 'other':
        cursor.execute(f"""
                        SELECT * FROM tag
                        WHERE name = '{tag_name['tag']}'
    """)
    else:
        cursor.execute(f"""
                            INSERT INTO tag (name)
                            VALUES ('{tag_name['other']}');
                            SELECT * FROM tag
                            WHERE name = '{tag_name['other']}'                   
        """)
    result = cursor.fetchall()
    return result


@connection_handler
def get_new_tags(cursor, id):
    cursor.execute(f"""
                    SELECT tag.id, tag.name FROM tag
                    WHERE tag.id NOT IN (
                        SELECT tag_id FROM question_tag
                        WHERE question_id = {id}
                        );
""")
    tags = cursor.fetchall()
    return tags


@connection_handler
def delete_tag_from_question(cursor, question_id, tag_id):
    cursor.execute(f"""
                    DELETE FROM question_tag
                    WHERE question_id = {question_id} AND tag_id = {tag_id};
""")
