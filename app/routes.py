from app import app, db
from app.models import Question 
from app.forms import EditQuestionForm, AddQuestionForm
from flask import render_template, flash, url_for, request, redirect
import random

@app.route('/', methods=['GET', 'POST'])
def index():
    question_count = db.session.query(Question).count()
    return render_template('start.html', question_count=question_count)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddQuestionForm()
    if form.validate_on_submit():
        # add the question to the database
        question = Question(question=form.question.data,
                            answer=form.answer.data,
                            topic=form.topic.data,
                            subtopic=form.subtopic.data)
        db.session.add(question)
        db.session.commit()
        flash('Question added')
        question_id = question.id
        return redirect(url_for('display_question', question_id=question.id))
    return render_template('add_question.html', form=form)


@app.route('/edit/<question_id>', methods=['GET', 'POST'])
def edit(question_id):
    form = EditQuestionForm()
    # fetch the question from the database
    question = Question.query.filter_by(id=question_id).first_or_404()

    if form.validate_on_submit():
        question.question = form.question.data
        question.answer = form.answer.data
        question.topic = form.topic.data
        question.subtopic = form.subtopic.data
        db.session.add(question)
        db.session.commit()
        flash('Question updated')
        return redirect(url_for('display_question', question_id=question.id))
    elif request.method == 'GET':
        form.question.data = question.question
        form.answer.data = question.answer
        form.topic.data = question.topic
        form.subtopic.data = question.subtopic
    return render_template('edit_question.html', form=form, question_id=question_id)

@app.route('/question', methods=['GET'])
@app.route('/question/<question_id>', methods=['GET'])
def display_question(question_id=None):
    # if no question_id is supplied, get the number of rows in the questions table
    if question_id is None: 
        question_count = db.session.query(Question).count()
        question_id = random.randint(1,question_count)
    question = Question.query.filter_by(id=question_id).first_or_404()
    return render_template('question.html', question=question)


