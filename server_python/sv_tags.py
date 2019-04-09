from server_python.config import app
from data_manager import dm_tags
from flask import request, redirect, render_template


@app.route('/question/<id>/new-tag', methods=['GET', 'POST'])
def route_add_tag(id):
    action = '/question/' + id + '/new-tag'
    options = dm_tags.get_new_tags(id)
    if request.method == 'POST':
        tag_id = dm_tags.get_tag_id_by_tag_name(request.form)
        dm_tags.add_tag_to_question(id, tag_id[0]['id'])
        return redirect('/')
    return render_template('tag.html', options=options, action=action)


@app.route('/question_detail/<question_id>/tag/<tag_id>/delete', methods=['GET'])
def route_delete_tag(question_id, tag_id):
    dm_tags.delete_tag_from_question(question_id, tag_id)
    return redirect(f'/question_detail/{question_id}')
