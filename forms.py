from flaskext.wtf import Form, TextField, TextAreaField, validators, SelectField, Required

class AnuncioForm(Form):
	tipo = SelectField(u'Tipo de Anuncio', choices=[('cpp', 'C++'), ('py', 'Python')])
	titulo = TextField()
	empresa = TextField()
	ciudad  = TextField() 
	web = TextField()
	descripcion = TextAreaField()
	pregunta = TextField()
	firma = TextField()
