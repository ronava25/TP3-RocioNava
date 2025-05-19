from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio),
    path("profesores", views.profesores, name="profesores"),
    path("cursos", views.cursos, name="cursos"),
    path("alta_curso", views.curso_formulario)
]
