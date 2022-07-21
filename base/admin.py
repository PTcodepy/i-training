from django.contrib import admin
from .models import Modelo, Curso, Formando


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('formacao', 'horario', 'duracao', 'localidade', 'localizacao', 'accao', 'curso')
    list_filter = ('curso',)
    list_editable = ('horario', 'duracao',)

@admin.register(Formando)
class FormandoAdmin(admin.ModelAdmin):
    pass
