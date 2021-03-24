from django.urls import path, re_path
from .views import CrearAutor, ListarAutor, EditarAutor, EliminarAutor
urlpatterns = [
    path('crear_autor/', CrearAutor.as_view(), name='crear_autor'),
    path('listar_autor/', ListarAutor.as_view(), name='listar_autor'),
    path('editar_autor/<int:pk>', EditarAutor.as_view(), name='editar_autor'),
    path('eliminar_autor/<int:pk>', EliminarAutor.as_view(), name='eliminar_autor'),



] 
