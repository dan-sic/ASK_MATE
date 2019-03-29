from flask import Flask, render_template, request, redirect
import data_manager
from flask_uploads import UploadSet, configure_uploads, IMAGES


app = Flask(__name__)
photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/images'
configure_uploads(app, photos)


@app.route('/')
def route_home():
    return render_template('index.html')


@app.route('/list')
def route_list():
    questions = data_manager.get_all_questions()
    return render_template('list.html', questions=questions)


@app.route('/add', methods=['GET', 'POST'])
def route_add_question():
    edit = False
    action = '/add'
    if request.method == 'POST':
        data_manager.add_question(request.form)
        return redirect('/list')
    return render_template('form.html', edit=edit, action=action)


@app.route('/question/<question_id>/delete')
def route_delete_question(question_id):
    data_manager.delete_element("questions", question_id)
    return redirect('/list')


@app.route('/answer/<combined_id>/delete')
def route_delete_answer(combined_id):
    answer_id = combined_id.split('_')[0]
    question_id = combined_id.split('_')[1]
    data_manager.delete_element("answers", answer_id)
    return redirect('/question_detail/' + question_id)


@app.route('/question_detail/<id>')
def route_question_detail(id):
    try:
        data_manager.question_view_count_increase(id)
        question = data_manager.get_question_by_id(id)
        answers = data_manager.get_answers_by_question_id(id)
        number_of_answers = len(answers)
        return render_template('qd.html', question=question, id=id, answers=answers, count=number_of_answers)
    except ValueError:
        return redirect('/')


@app.route('/question_detail/<id>/edit', methods=['POST', 'GET'])
def route_question_edit(id):
    edit = True
    action = '/question_detail/' + id + '/edit'
    question = data_manager.get_question_by_id(id)
    if request.method == 'POST':
        data_manager.update_question(id, request.form)
        return redirect('/question_detail/' + id)
    return render_template('form.html', edit=edit, question=question, id=id, action=action)


@app.route('/question/<str:id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(id):
    if request.method == 'POST':
        # todo: check is question exists
        data_manager.add_answer(request.form, id)
        return redirect('/question_detail/' + id)
    return render_template('answer.html', id=id)


@app.route('/sort')
def my_route():
    feature_to_order_by = request.args.get('order_by', default='title', type=str)
    order_direction = request.args.get('order_direction', default='asc', type=str)
    questions = data_manager.sort_questions(feature_to_order_by, order_direction)
    return render_template('list.html', questions=questions)


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
        
        data_manager.update_image(file_type, filename, id)
        return redirect('/question_detail/' + question_id)
    return redirect('/list')


@app.route('/question/<question_id>/vote-down')
def question_vote_down(question_id):
    data_manager.change_vote("questions", question_id, -1)
    return redirect('/question_detail/' + question_id)


@app.route('/question/<question_id>/vote-up')
def question_vote_up(question_id):
    data_manager.change_vote("questions", question_id, 1)
    return redirect('/question_detail/' + question_id)


@app.route('/answer/<answer_id>/vote-down/<question_id>')
def answer_vote_down(answer_id, question_id):
    data_manager.change_vote("answers", answer_id, -1)
    return redirect('/question_detail/' + question_id)


# issue to talk about during code review - should we use POST method here
@app.route('/answer/<answer_id>/vote-up/<question_id>')
def answer_vote_up(answer_id, question_id):
    data_manager.change_vote("answers", answer_id, 1)
    return redirect('/question_detail/' + question_id)


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5004
)