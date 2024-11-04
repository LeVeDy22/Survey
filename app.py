from models import (
    Answer,
    db,
    Survey,
)
from flask import (
    Flask,
    jsonify,
    render_template,
    request,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route('/')
def index():
    surveys = Survey.query.all()
    return render_template('index.html', surveys=surveys)


@app.route('/check_answers', methods=['POST'])
def check_answers():
    data = request.get_json()
    answers = data.get('answers', [])
    correct_count = 0

    for answer_data in answers:
        answer_id = answer_data.get('answer_id')
        answer = Answer.query.get(answer_id)
        if answer and answer.is_correct:
            correct_count += 1

    return jsonify({"correct_count": correct_count})


if __name__ == "__main__":
    app.run()
