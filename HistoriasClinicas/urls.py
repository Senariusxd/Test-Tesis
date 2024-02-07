from django.contrib import admin
from django.urls import path

from Control import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('', views.inicio_view, name='inicio'),
    path('about/', views.about_view, name='about'),
    
    
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/agregar/', views.agregar_paciente, name='agregar_paciente'),
    path('pacientes/editar/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:paciente_id>/', views.eliminar_paciente, name='eliminar_paciente'),
    
    
    path('historias_clinicas/', views.lista_historias_clinicas, name='lista_historias_clinicas'),
    path('historias_clinicas/crear/', views.crear_historia_clinica, name='crear_historia_clinica'),
    path('historia_clinica/modificar/<int:historia_id>/', views.modificar_historia_clinica, name='modificar_historia_clinica'),
    path('historias_clinicas/eliminar/<int:historia_id>/', views.eliminar_historia_clinica, name='eliminar_historia_clinica'),
    
    path('historia_clinica/<int:historia_id>/', views.ver_historia_clinica, name='ver_historia_clinica'),
    
    
    
    
]