from flask import Flask

def create_application():
	app = Flask(__name__)
	app.debug=True
	app.config['CSRF_SESSION_LKEY']="fadfasdfasfda"
	app.secret_key ="FDSFASD$%&/"
	return app

app = create_application()