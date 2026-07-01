import git
import request
import flask
flask import Flask, render_template,url_for, flask, redirect,request


@app.route("/update_server", methods=['POST'])
def webhook():
	if request.method == 'POST':
		repo = git.Repo('/home/FlaskProjectDM/Flask--Project')
		origin = repo.remotes.origin
		origin.pull()
		reutrn 'Update PythonAnywhere successfully', 200
	else:
	    return 'Wrong event type', 400
