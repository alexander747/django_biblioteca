from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor
from django.core.exceptions import ObjectDoesNotExist

#vistas basadas en clase
from django.views.generic import View, TemplateView


"""
    de View heredan las demas vistas basadas en clases, se utiliza cuando vamos a utilizar logica en el codigo
    metodo get: siempre recibe self, request, *args, **kwargs 

    1) dispatch: metodo que verifica que tipo de peticion es (post, get, put)
    2) http_method_not_allowed(): retorna un error cuando se utiliza un metodo http no soportado
    3) options()


    TemplateView: solo renderiza un template

"""


# class Inicio(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'index.html')



class Inicio(TemplateView):
     template_name = 'index.html'

def crearAutor(request):
    if request.method =='POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save() #save data
            return redirect('index') #name index desde las urls, redirije 
    else:
            autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form':autor_form})            


def listarAutor(request):
    # autores = Autor.objects.all()
    autores = Autor.objects.filter(estado=True)

    return render(request,'libro/listar_autor.html', {'autores':autores})


def editarAutor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method=='GET':
            autor_form = AutorForm(instance = autor) #llenamos el formulario con los datos del autor consultado
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor') 
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'libro/crear_autor.html',{'autor_form':autor_form, 'error':error})           

## eliminacion directa
# def eliminarAutor(request, id):
#     autor = Autor.objects.get(id=id)
#     if request.method =='POST':
#         autor.delete() 
#         return redirect('libro:listar_autor')    
#     return render(request, 'libro/eliminar_autor.html', {'autor':autor})    

def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method =='POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')    
    return render(request, 'libro/eliminar_autor.html', {'autor':autor})    
