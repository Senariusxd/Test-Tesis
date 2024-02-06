from django.contrib import admin
from django.urls import path
from Control import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('', views.inicio_view, name='inicio'),
    path('about/', views.about_view, name='about'),
    path('historia-clinica/<int:paciente_id>/', views.historia_clinica, name='historia_clinica'),
    path('agregar-paciente/', views.agregar_paciente, name='agregar_paciente'),
    path('lista-pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('agregar-historia-clinica/', views.agregar_historia_clinica, name='agregar_historia_clinica'),
    path('historias_clinicas/', views.todas_historias_clinicas, name='todas_historias_clinicas'),
    path('paciente/<str:id_paciente>/eliminar/', views.eliminar_paciente, name='eliminar-paciente'),
]