from server_python.config import app, photos
from data_manager import dm_general
from flask import request, redirect, render_template


@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        question_id = request.args.get('question_id', type=str)
        answer_id = request.args.get('answer_id', type=str)
        try:
            filename = photos.save(request.files['photo'])
        except Exception:
            return redirect('/question_detail/' + question_id)

        id = answer_id if answer_id else question_id
        table = "answer" if answer_id else "question"

        dm_general.update_image_path(table, filename, id)
        return redirect('/question_detail/' + question_id)
