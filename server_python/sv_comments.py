from server_python.config import app
from data_manager import dm_answers, dm_comments
from flask import request, redirect, render_template


@app.route('/question/<id>/new-comment', methods=['GET', 'POST'])
def route_add_comment(id):
    action = '/question/' + id + '/new-comment'
    if request.method == 'POST':
        dm_comments.add_comment_to_question(request.form, id)
        return redirect(f'/question_detail/{id}')
    return render_template('comment.html', id=id, action=action)


@app.route('/answer/new-comment', methods=['GET', 'POST'])
def route_add_comment_to_answer():
    question_id = request.args.get('question_id')
    answer_id = request.args.get('answer_id')
    if request.method == 'POST':
        dm_comments.add_comment_to_answer(request.form, answer_id, question_id)
        return redirect(f"/question_detail/{question_id}")
    return render_template('comment.html', question_id=question_id, answer_id=answer_id)


@app.route('/comments/<id>/edit', methods=['GET', 'POST'])
def route_edit_comment(id):
    action = '/comments/' + id + '/edit'
    comment = dm_comments.get_comment_by_id(id)[0]
    if request.method == 'POST':
        result = dm_comments.update_comment_by_id(request.form, id)[0]
        return redirect(f"/question_detail/{result['question_id']}")
    return render_template('comment.html', comment=comment, action=action)


@app.route('/comments/<id>/delete', methods=['GET'])
def route_delete_comment(id):
    directory = dm_comments.get_comment_by_id(id)[0]
    dm_comments.delete_comment_by_id(id)
    return redirect(f"/question_detail/{directory['question_id']}")
