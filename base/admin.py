from django.contrib import admin
from .models import Formador, Curso, Formando


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'horario', 'localidade', 'localizacao', 'accao',)
    list_editable = ('duracao', 'horario', 'localidade', 'localizacao',)



@admin.register(Formador)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso',)
    list_filter = ('curso',)
    list_editable = ('curso',)

@admin.register(Formando)
class FormandoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'habilitacoes', 'email', 'contacto', 'localidade', 'data_nascimento', 'nacionalidade',
                    'curso', 'formador',)
    list_filter = ('curso',)
    list_editable = ('curso', 'formador',)





