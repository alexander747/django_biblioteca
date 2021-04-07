from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from .views import CrearAutor, ListarAutor, EditarAutor, EliminarAutor, ListadoLibros, CrearLibro
urlpatterns = [
    path('crear_autor/', login_required(CrearAutor.as_view()), name='crear_autor'),
    path('listar_autor/', login_required(ListarAutor.as_view()), name='listar_autor'),
    path('editar_autor/<int:pk>', login_required(EditarAutor.as_view()), name='editar_autor'),
    path('eliminar_autor/<int:pk>', login_required(EliminarAutor.as_view()), name='eliminar_autor'),

    path('listar_libros/', login_required(ListadoLibros.as_view()), name='listado_libros'),
    path('crear_libro/', login_required(CrearLibro.as_view()), name='crear_libro'),



] 
