from server_python.config import app, photos
from data_manager import dm_general
from flask import request, redirect, render_template


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        question_id = request.args.get('question_id', type=str)
        answer_id = request.args.get('answer_id', type=str)
        try:
            filename = photos.save(request.files['photo'])
        except:
            return redirect('/question_detail/' + question_id)

        id = answer_id if answer_id else question_id
        file_type = "answers" if answer_id else "questions"

        dm_general.update_image(file_type, filename, id)
        return redirect('/question_detail/' + question_id)
    return redirect('/list')
