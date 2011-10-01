from flask.views import MethodView
from flask import jsonify
from models import Anuncio
from utils import register_api
from django.utils import simplejson as json

class AnuncioAPI(MethodView):
	
	def get(self, key):
	
		anuncios = Anuncio.all()
		return json.dumps([a.to_dict() for a in anuncios])
	
				
	def post(self):
		anuncio = Anuncio()
		anuncio.nombre = request.form['nombre']
		anucio.put()
		
	def delete(self, key):
		anuncio = Anuncio.get(key)
		
		return jsonify({'response' : 'ok'})
		
	def put(self, key):
		pass
		
register_api(AnuncioAPI, 'anuncio', '/anuncio/')


	
	