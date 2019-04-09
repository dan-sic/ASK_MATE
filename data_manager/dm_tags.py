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
    print(tags, 'these is what we rteturner')
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
    print(tag_name)
    cursor.execute(f"""
                    SELECT * FROM tag
                    WHERE name = '{tag_name['tag']}'
""")
    tag_id = cursor.fetchall()
    # if there is no tag in table, add new one
    if tag_id:
        return tag_id
    else:
        cursor.execute(f"""
                    INSERT INTO tag (name)
                    VALUES ('{tag_name['tag']}');
                    SELECT * FROM tag
                    WHERE name = '{tag_name['tag']}'                   
""")
        tag_id = cursor.fetchall()
        return tag_id


@connection_handler
def get_new_tags(cursor, id):
    cursor.execute(f"""
                    SELECT * from question_tag FULL OUTER JOIN tag ON question_tag.tag_id = tag.id
                    WHERE question_tag.question_id <> 1 OR question_tag.question_id is NULL
                        AND tag_id NOT IN(
                            SELECT tag_id
                            FROM question_tag
                            WHERE question_id = 1);
""")
    tags = cursor.fetchall()
    print(tags)
    return tags


@connection_handler
def delete_tag_from_question(cursor, question_id, tag_id):
    cursor.execute(f"""
                    DELETE FROM question_tag
                    WHERE question_id = {question_id} AND tag_id = {tag_id};
""")
