from server_python.config import app
from data_manager import dm_general, dm_answers
from flask import redirect, request, render_template

# todo - deleting answer and question
@app.route('/answer/delete')
def route_delete_answer():
    answer_id = request.args.get('answer_id')
    question_id = request.args.get('question_id')
    dm_general.delete_element("answers", answer_id)
    return redirect('/question_detail/' + question_id)


@app.route('/question/<id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(id):
    if request.method == 'POST':
        dm_answers.add_sql_answer(request.form, id)
        return redirect('/question_detail/' + id)
    return render_template('answer.html', id=id)


@app.route('/answer/<answer_id>/vote-down/<question_id>')
def answer_vote_down(answer_id, question_id):
    dm_general.change_vote("answer", answer_id, -1)
    return redirect('/question_detail/' + question_id)


# issue to talk about during code review - should we use POST method here - YES - todo
@app.route('/answer/<answer_id>/vote-up/<question_id>')
def answer_vote_up(answer_id, question_id):
    dm_general.change_vote("answer", answer_id, 1)
    return redirect('/question_detail/' + question_id)
