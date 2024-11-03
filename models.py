from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Survey(db.Model):
    __tablename__ = "survey"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False)


class Answer(db.Model):
    __tablename__ = "answer"
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"))
    survey = db.relationship("Survey", backref=db.backref("answer", lazy=True))

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(100), nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
