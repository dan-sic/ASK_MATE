from server_python.config import app
from data_manager import dm_general, dm_answers
from flask import redirect, request, render_template


@app.route('/answer/<combined_id>/delete')
def route_delete_answer(combined_id):
    answer_id = combined_id.split('_')[0]
    question_id = combined_id.split('_')[1]
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
    dm_general.change_vote("answers", answer_id, -1)
    return redirect('/question_detail/' + question_id)


# issue to talk about during code review - should we use POST method here
@app.route('/answer/<answer_id>/vote-up/<question_id>')
def answer_vote_up(answer_id, question_id):
    dm_general.change_vote("answers", answer_id, 1)
    return redirect('/question_detail/' + question_id)
