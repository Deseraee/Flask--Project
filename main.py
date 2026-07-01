import git
import requests

from flask import Flask, render_template, url_for, redirect,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

with app.app_context():
  db.create_all()

if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()



@app.route("/update_server", methods=['POST'])
def webhook():
	if request.method == 'POST':
		repo = git.Repo('/home/FlaskProjectDM/Flask--Project')
		origin = repo.remotes.origin
		origin.pull()
		return 'Update PythonAnywhere successfully', 200
	else:
	    return 'Wrong event type', 400
