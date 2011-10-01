from google.appengine.ext import db
	
class Anuncio(db.Model):
	tipo =  db.StringProperty(multiline=False)
	titulo =  db.StringProperty(multiline=False)
	empresa =  db.StringProperty(multiline=False)
	ciudad = db.StringProperty(multiline=False)
	web = db.StringProperty(multiline=False)
	descripcion = db.StringProperty(multiline=True)
	fecha = db.DateTimeProperty(auto_now_add=True)
	pregunta = db.StringProperty(multiline=False)
	firma = db.StringProperty(multiline=True)
	
	def to_dict(self):
	       return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
	
	
class Postulacion(db.Model):
	anuncio = db.ReferenceProperty(Anuncio)
	usuario = db.StringProperty(multiline=True)
	respuesta =  db.StringProperty(multiline=True)
	
	def to_dict(self):
	       return dict([(p, unicode(getattr(self, p))) for p in self.properties()])
	