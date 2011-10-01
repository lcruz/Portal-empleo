from google.appengine.api import users
from flask import redirect
from functools import wraps

def is_authenticated(f):
	
	@wraps(f)
	def view(*args, **kwargs):
		user = users.get_current_user()
		if user:
			return f(*args, **kwargs)
		else:
			return redirect(users.create_login_url("/"))

	return view