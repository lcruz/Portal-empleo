import uuid
from config import app

def build_file_name(filename):
	return 'file_' + str(uuid.uuid1()) + '.' + filename.split('.')[-1]
	
def register_api(view, endpoint, url, pk='key'):
	view_func = view.as_view(endpoint)
	app.add_url_rule(url, defaults={'key' : None}, view_func=view_func, methods=['GET', 'POST'])	
	app.add_url_rule('%s<%s>' % (url, pk), view_func=view_func, methods=['GET', 'PUT', 'DELETE'])
