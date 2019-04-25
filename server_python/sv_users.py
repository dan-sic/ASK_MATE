from server_python.config import app
from data_manager import dm_users
# from flask import render_template
from flask import request, redirect, render_template, jsonify


@app.route('/users_list', methods=['GET', 'POST'])
def route_list_users():
    users = dm_users.get_users()
    return render_template('users.html', users=users)


@app.route('/sort_users', methods=['GET', 'POST'])
def route_sort_users():
    feature_to_order_by = request.args.get('order_by', default='username', type=str)
    order_direction = request.args.get('order_direction', default='asc', type=str)
    users = dm_users.get_users_sorted(feature_to_order_by, order_direction)
    return render_template('users.html',
                           users=users)


@app.route('/user_page', methods=['GET', 'POST'])
def user_page():
    user_id = request.args.get('user_id')
    user_data = dm_users.get_user(user_id=user_id)
    user_questions, questions_count = dm_users.get_user_questions(user_id)
    user_answers, answers_count = dm_users.get_user_answers_wth_corresponding_question_titles(user_id)
    user_comments, comments_count = dm_users.get_user_comments_with_corresponding_question(user_id)
    return render_template('user_page.html',
                           user=user_data,
                           questions=user_questions,
                           answers=user_answers,
                           comments=user_comments,
                           questions_count=questions_count,
                           answers_count=answers_count,
                           comments_count=comments_count)