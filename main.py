import sys, os

package_dir = "packages"
package_dir_path = os.path.join(os.path.dirname(__file__), package_dir)
sys.path.insert(0, package_dir_path)

from flask import Flask, request, render_template, redirect, url_for, Response, flash
from werkzeug import secure_filename
from utils import build_file_name
from config import app
from google.appengine.ext.webapp.util import run_wsgi_app
from forms import AnuncioForm
from models import Anuncio
from decorators import is_authenticated
import services

@app.route("/")
def index():
	anuncios = Anuncio.all()
	return render_template('index.html', anuncios=anuncios)


@app.route("/publicar/", methods=("GET", "POST"))	
@is_authenticated
def publicar():
	form = AnuncioForm();

	if form.is_submitted():
		anuncio = Anuncio(tipo = form.tipo.data,
						empresa = form.empresa.data,
						titulo = form.titulo.data,
						ciudad = form.ciudad.data,
						web = form.web.data,
						descripcion = form.descripcion.data,
						pregunta = form.pregunta.data,
						firma = form.firma.data)
		anuncio.put()
		flash("Anuncio guardado.")
		return redirect("/")
	return render_template('publicar.html', form = form)

@app.route("/detalle/<key>")
def detalle(key):
	anuncio = Anuncio.get(key)
	return render_template('detalle.html', anuncio = anuncio)
	
#@app.context_processor
#def do_something():
#	pass

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
	
if __name__ == "__main__":
	from wsgiref.handlers import CGIHandler
	from werkzeug_debugger_appengine import get_debugged_app
	app = get_debugged_app(app)
	CGIHandler().run(app)
	