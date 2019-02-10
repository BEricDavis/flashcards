from app import app, db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256))
    answer = db.Column(db.String(256))
    topic = db.Column(db.String(64))
    subtopic = db.Column(db.String(64))

    def __repr__(self):
        return '<Question {}: {}>'.format(self.id, self.question)
        