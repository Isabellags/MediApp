from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('profesionales', profesionales, name="profesionales"),
    path('mant/profesional/agregar/', agregar_profesional, name="agregar_profesional" ),
    path('mant/profesional/listar/', listar_profesional, name="listar_profesional"),
    path('modificar_profesional/<rut>/',modificar_profesional, name="modificar_profesional"),
    path('eliminar_profesional/<rut>/', eliminar_profesional, name="eliminar_profesional"),
    path('login_usuario/', login_usuario, name='login_usuario'),
    path('registro_profesional/', registro_profesional, name="reg_prof"),

]