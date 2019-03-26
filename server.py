from flask import Flask, render_template, request, redirect
import data_manager

app = Flask(__name__)


@app.route('/')
def route_home():
    return render_template('index.html')


@app.route('/list')
def route_list():
    stories = data_manager.get_all_questions()
    return render_template('list.html', stories=stories)


@app.route('/add')
def route_add():
    return render_template('form.html')


@app.route('/add', methods=['GET', 'POST'])
def route_add_question():
    if request.method == 'POST':
        current_file = data_manager.get_all_questions()
        new_dict = {}
        new_dict['id'] = str(int(current_file[0]['id']) + 1)
        new_dict['title'] = request.form['title']
        new_dict['message'] = request.form['description']
        new_dict['submission_time'] = 'now'
        new_dict['view_number'] = '1'
        new_dict['vote_number'] = '1'
        new_dict['image'] = ''
        current_file.append(new_dict)
        data_manager.save_new_question(current_file)
        return redirect('/')
    return render_template('form.html')


@app.route('/add-question/<id>')
def route_question_detail(id):
    try:
        element = data_manager.get_question_by_id(id)
        answers = data_manager.get_answers_by_question_id(id)
        return render_template('qd.html', element=element, id=id, answers=answers)
    except ValueError:
        return redirect('/')


@app.route('/question/<id>/new-answer', methods=['GET', 'POST'])
def route_new_answer(id):
    if request.method == 'POST':
        current_file = data_manager.get_all_answers()
        new_answer = {}
        if current_file:
            new_answer['id'] = str(int(current_file[-1]['id']) + 1)
        else:
            new_answer['id'] = '0'
        new_answer['submission_time'] = ''
        new_answer['vote_number'] = '0'
        new_answer['question_id'] = id
        new_answer['message'] = request.form['answer']
        new_answer['image'] = ''
        current_file.append(new_answer)
        data_manager.save_new_answer(current_file)
        return redirect('/add-question/' + id)
    return render_template('answer.html')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5004
)
