from models import Anuncio
import appengine_admin

class AnuncioAdmin(appengine_admin.ModelAdmin):
    model = Anuncio
    listFields = ('empresa',)
    editFields = ('empresa', 'web', 'tipo')
    readonlyFields = ('fecha',)

appengine_admin.register(AnuncioAdmin)