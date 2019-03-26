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


@app.route('/story/<id>')
def route_edit(id):
    cokolwiek = 'hello world' + id
    return cokolwiek


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5004
)
