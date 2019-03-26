import connection


def get_all_questions():
    q_list = sorted(connection.read_file(), key=lambda k: k['submission_time'], reverse=True)
    return q_list


