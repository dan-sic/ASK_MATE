import re
from server_python.config import base_url
from flask import request


def check_referer_url(question_id):
    referer_url = request.headers.get("Referer")
    if referer_url != f"{base_url}/question_detail/{question_id}":
        return True
    else:
        return False


def replace_string(matchobj):
    return '<span class="bg-success" style="margin-right:0;">' + matchobj.group(0) + '</span>'


def highlight_search_term(searched_term, sequence):
    searched_term_escaped = re.escape(r'{}'.format(searched_term))
    new_sequence = re.sub(searched_term_escaped, replace_string, sequence, flags=re.I)
    return new_sequence


def truncate_question(question_message, max_length):
    if len(question_message) > max_length:
        return question_message[:max_length] + ' (...)'
    else:
        return question_message

# todo > unused parameters, wrong placement of function, fix it
def change_reputation(user_id, value):
    cursor.execute("""
                    UPDATE question
                    SET  title = %(title)s, message = %(message)s 
                    WHERE id = %(id)s
                    """,
                   {'title': form_data['title'], 'message': form_data['message'], 'id': id})