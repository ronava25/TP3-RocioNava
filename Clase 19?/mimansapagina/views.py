from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mimansapagina/index.html')

def profesores(request):
    return render(request,"profesores.html")

def curso(request):
    return render(request,"cursos.html")

def alta_curso(request):
    return render(request,"alta_curso.html")


def curso_formulario(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["nombre"],camada=request.POST["camada"])
        curso.save()
        return render(request, "formulario.html")

    return render(request, "formulario.html")