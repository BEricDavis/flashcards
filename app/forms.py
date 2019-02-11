from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm  
from app.models import Question

class AddQuestionForm(FlaskForm):
    question = TextAreaField('Question', render_kw={"rows": 2, "cols": 80}, validators=[DataRequired()])
    answer = TextAreaField('Answer', render_kw={"rows": 2, "cols": 80}, validators=[DataRequired()])
    topic = StringField('Topic', validators=[DataRequired()])
    subtopic = StringField('Subtopic')
    submit = SubmitField('Submit')

class EditQuestionForm(FlaskForm):
    question = TextAreaField('Question', render_kw={"rows": 2, "cols": 80}, validators=[DataRequired()])
    answer = TextAreaField('Answer', render_kw={"rows": 2, "cols": 80}, validators=[DataRequired()])
    topic = StringField('Topic', validators=[DataRequired()])
    subtopic = StringField('Subtopic')
    submit = SubmitField('Submit')