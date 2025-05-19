def profesores(request):
    return render(request,"profesores.html")

def curso(request):
    return render(request,"cursos.html")

def alta_curso(request):
    return render(request,"alta_curso.html")


def curso_formulario(request):
    if request.method == "POST":
        pass

    return render(request, xxxx)