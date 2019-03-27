import time

def convert_time_value_to_formatted_string(question):
    print(question['submission_time'])
    question['submission_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(question['submission_time'])))
    return question

