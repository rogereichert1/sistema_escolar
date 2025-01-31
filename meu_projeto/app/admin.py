from django.contrib import admin
from .models import Usuario, Filho, Atividade, Meta

admin.site.register(Usuario)
admin.site.register(Filho)
admin.site.register(Atividade)
admin.site.register(Meta)
