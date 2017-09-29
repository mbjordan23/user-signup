from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
	return render_template('signup.html')


@app.route('/', methods=['POST'])
def function():
	username = request.form['username']
	password = request.form['password']
	verifypassword = request.form['verifypassword']
	email = request.form['email']

	username_error = ''
	password_error = ''
	email_error = ''

	if username == '':
		username_error = 'Please enter a username'
		username = ''
	elif ' ' in username == True:
		username_error = 'Invalid username - no spaces'
		username = ''
	else:
		if len(username) > 20 or len(username) < 3:
			username_error = 'Username must be between 3 and 20 characters'
			username = ''

	if password == '':
		password_error = 'Please enter a password'
		password = ''
		verifypassword = ''
	elif ' ' in password == True:
		password_error = 'Invalid password - no spaces'
		password = ''
		verifypassword = ''
	elif password != verifypassword:
		password_error = 'Passwords do not match'
		password = ''
		verifypassword = ''
	else:
		if len(password) > 20 or len(password) < 3:
			username_error = 'Password must be between 3 and 20 characters'
			password = ''
			verifypassword = ''

	if email == '':
		email_error = ''
	elif ' ' in email:
		email_error = 'Invalid email address - no spaces'
		email = ''
	elif '@' not in email or '.' not in email:
		email_error = 'Invalid email address'
		email = ''
	else:
		if len(email) > 20 or len(email) < 3:
			email_error = 'Email address must be between 3 and 20 characters'
			email = ''

	if username_error == '' and password_error == '' and email_error == '':
		name = username
		return render_template('welcome.html', name=name)
	else:
		return render_template('signup.html',
			username=username,
			email=email, 
			username_error=username_error, 
			password_error=password_error, 
			email_error=email_error)


#@app.route('/welcome', methods=['GET'])
#def welcome():
#	name = request.form['name']
#	return render_template('welcome.html', name=username)


app.run()