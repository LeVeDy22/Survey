from models import Survey, Answer, db
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

if __name__ == "__main__":
    app.run()
