from django.contrib import admin
from .models import Aluno, Disciplina, Professor, Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'matricula')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    pass

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass