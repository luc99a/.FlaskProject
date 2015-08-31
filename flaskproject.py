from flask import Flask
from flask import request

application = Flask(__name__)

@application.route("/")
def root():
	return "<h1>Welcome</h1>"

@application.route("/admin", methods = ["GET", "POST"])
def admin():
	html = None
	username = request.form.get("username")
	password = request.form.get("password")
	#hardcoded username and password just to test
	if username == "admin" and password == "password":
		html = "<h1>Successfully logged in</h1>"
	elif username == None or password == None:
		html = """
			<h1>Are you the admin?</h1>
			<h6>Please log in</h6>
			<form method="post" >
				Username: <input type="text" name="username" > <br />
				Password: <input type="password" name="password" > <br />
				<input type="submit" value="Log in" > <br />
			</form>
			"""
	else:
		html = "<h1>Wrong username or password</h1>"
	return html
