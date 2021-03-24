from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy

#vistas basadas en clase
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView


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
      

class CrearAutor(CreateView):
    model = Autor
    form_class=AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')        


class ListarAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado=True)

class EditarAutor(UpdateView):
    model = Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')

   

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
