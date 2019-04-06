from server_python.config import app
from data_manager import dm_general
from flask import request, redirect, render_template
import datetime
from data_manager import dm_comments


@app.route('/question/<id>/new-comment', methods=['GET', 'POST'])
def route_add_comment(id):
    action = '/question/' + id + '/new-comment'
    if request.method == 'POST':
        dm_comments.add_comment_to_question(request.form, id)
        return redirect(f'/question_detail/{id}')
    return render_template('comment.html', id=id, action=action)


@app.route('/answer/<id>/new-comment', methods=['GET', 'POST'])
def route_add_comment_to_answer(id):
    action = '/answer/' + id + '/new-comment'
    if request.method == 'POST':
        dm_comments.add_comment_to_answer(request.form, id)
        return redirect(f'/question_detail/{id}')
    return render_template('comment.html', id=id, action=action)


@app.route('/comments/<id>/edit', methods=['GET', 'POST'])
def route_edit_comment(id):
    action = '/comments/' + id + '/edit'
    comment = dm_comments.get_comment_by_id(id)[0]
    if request.method == 'POST':
        result = dm_comments.update_comment_by_id(request.form, id)[0]
        return redirect(f"/question_detail/{result['question_id']}")
    return render_template('comment.html', comment=comment, action=action)
