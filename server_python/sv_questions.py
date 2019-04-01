from server_python.config import app
from data_manager import dm_general, dm_questions, dm_answers
from flask import request, redirect, render_template


@app.route('/list')
def route_list():
    questions = dm_questions.get_all_questions_sql_sorted_by_submission_time()
    return render_template('list.html', questions=questions)


@app.route('/sort')
def route_sort_questions():
    feature_to_order_by = request.args.get('order_by', default='title', type=str)
    order_direction = request.args.get('order_direction', default='asc', type=str)
    questions = dm_questions.sort_questions(feature_to_order_by, order_direction)
    return render_template('list.html', questions=questions)


@app.route('/add', methods=['GET', 'POST'])
def route_add_question():
    edit = False
    action = '/add'
    if request.method == 'POST':
        dm_questions.add_question_sql(request.form)
        return redirect('/list')
    return render_template('form.html', edit=edit, action=action)


@app.route('/question/<question_id>/delete')
def route_delete_question(question_id):
    dm_general.delete_element("questions", question_id)
    return redirect('/list')


@app.route('/question_detail/<id>', methods=['GET', 'POST'])
def route_question_detail(id):
    try:
        if request.method == 'GET':
            dm_questions.question_view_count_increase(id)
        question = dm_questions.get_question_sql_by_id(id)
        answers = dm_answers.get_answers_by_question_id(id)
        number_of_answers = len(answers)
        return render_template('qd.html', question=question, id=id, answers=answers, count=number_of_answers)
    except ValueError:
        return redirect('/')


@app.route('/question_detail/<id>/edit', methods=['POST', 'GET'])
def route_question_edit(id):
    edit = True
    action = '/question_detail/' + id + '/edit'
    question = dm_questions.get_question_by_id(id)
    if request.method == 'POST':
        dm_questions.update_question(id, request.form)
        return redirect('/question_detail/' + id)
    return render_template('form.html', edit=edit, question=question, id=id, action=action)


@app.route('/question/<question_id>/vote-down')
def question_vote_down(question_id):
    dm_general.change_vote("questions", question_id, -1)
    return redirect('/question_detail/' + question_id)


@app.route('/question/<question_id>/vote-up')
def question_vote_up(question_id):
    dm_general.change_vote("questions", question_id, 1)
    return redirect('/question_detail/' + question_id)
