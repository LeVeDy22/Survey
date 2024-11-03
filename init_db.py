from models import Survey, Answer, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()
    survey1 = Survey(question="What is the capital of France?")
    survey2 = Survey(question="What is the largest planet in our Solar System?")
    survey3 = Survey(question="Which element has the chemical symbol O?")

    db.session.add_all([survey1, survey2, survey3])
    db.session.commit()

    db.session.add_all(
        [
            Answer(survey_id=survey1.id, answer="Berlin", is_correct=False),
            Answer(survey_id=survey1.id, answer="Madrid", is_correct=False),
            Answer(survey_id=survey1.id, answer="Paris", is_correct=True),
            Answer(survey_id=survey1.id, answer="Rome", is_correct=False),
        ]
    )
    db.session.add_all(
        [
            Answer(survey_id=survey2.id, answer="Earth", is_correct=False),
            Answer(survey_id=survey2.id, answer="Jupiter", is_correct=True),
            Answer(survey_id=survey2.id, answer="Mars", is_correct=False),
            Answer(survey_id=survey2.id, answer="Venus", is_correct=False),
        ]
    )
    db.session.add_all(
        [
            Answer(survey_id=survey3.id, answer="Hydrogen", is_correct=False),
            Answer(survey_id=survey3.id, answer="Oxygen", is_correct=True),
            Answer(survey_id=survey3.id, answer="Nitrogen", is_correct=False),
            Answer(survey_id=survey3.id, answer="Carbon", is_correct=False),
        ]
    )
    db.session.commit()
