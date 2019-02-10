from app import app, db
from app.models import Question 
from app.forms import EditQuestionForm, AddQuestionForm
from flask import render_template, flash, url_for, request, redirect
import random

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('start.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = EditQuestionForm()
    if form.validate_on_submit():
        # add the question to the database
        print('validated')
        question = Question(question=form.question.data,
                            answer=form.answer.data,
                            topic=form.topic.data,
                            subtopic=form.subtopic.data)
        db.session.add(question)
        db.session.commit()
        flash('Question added')
        question_id = question.id
        return redirect(url_for('display_question'))
    print('not validated')
    return render_template('edit_question.html', form=form)


@app.route('/edit/<question_id>', methods=['GET', 'POST'])
def edit(question_id):
    form = EditQuestionForm()
    # fetch the question from the database
    question = Question.query.filter_by(id=question_id).first_or_404()
    form.question = question.question
    form.answer = question.answer
    form.topic = question.topic
    form.subtopic = question.subtopic
    return render_template('edit_question.html', form=form, question_id=question_id)

@app.route('/question', methods=['GET'])
@app.route('/question/<question_id>', methods=['GET'])
def display_question(question_id=None):
    # get the number of rows in the questions table
    if question_id is None: 
        question_count = db.session.query(Question).count()
        print('question_count: {}'.format(question_count))
        question_id = random.randint(1,question_count+1)
    print('question_id={}'.format(question_id))
    question = Question.query.filter_by(id=question_id).first_or_404()
    print(question)
    return render_template('question.html', question=question)


