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
        return render_template('qd.html', element=element, id=id)
    except ValueError:
        return redirect('/')


@app.route('/question/<id>/new-answer')
def route_new_answer(id):
    pass


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5004
)
