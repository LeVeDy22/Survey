from models import Survey, Answer, db
from app import app

with app.app_context():
    db.create_all()
    survey1 = Survey(question="What is your favorite color?")
    survey2 = Survey(question="What is your favorite animal?")
    survey3 = Survey(question="What is your favorite season?")

    db.session.add_all([survey1, survey2, survey3])
    db.session.commit()

    answer1 = Answer(survey_id=survey1.id, answer="Blue")
    answer2 = Answer(survey_id=survey1.id, answer="Green")
    answer3 = Answer(survey_id=survey2.id, answer="Cat")
    answer4 = Answer(survey_id=survey2.id, answer="Dog")
    answer5 = Answer(survey_id=survey3.id, answer="Spring")
    answer6 = Answer(survey_id=survey3.id, answer="Winter")

    db.session.add_all([answer1, answer2, answer3, answer4, answer5, answer6])
    db.session.commit()

    print("Happy " * 10000000)
