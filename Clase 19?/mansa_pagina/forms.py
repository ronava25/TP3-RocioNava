from django import forms

class Curso_formularios(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()