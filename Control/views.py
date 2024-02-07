from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Paciente , HistoriaClinica
from .forms import PacienteForm, ModificarPacienteForm, HistoriaClinicaForm

import datetime


def home(request):
    return render(request, "home.html")

def inicio_view(request):
    # Obtener datos o realizar operaciones necesarias para la vista
    datos = {
        'titulo': 'Página de inicio',
        'mensaje': 'Bienvenido a mi sitio web',
    }
    return render(request, 'inicio.html', datos)

def about_view(request):
    datos = {
        'titulo': 'Acerca de',
        'descripcion': 'Esta es una página de información sobre nosotros.',
    }
    return render(request, 'about.html', datos)


def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    
    context = {
        'form': form
    }
    return render(request, 'agregar_paciente.html', context)

def modificar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(ID_PACIENTE=id_paciente)

    if request.method == 'POST':
        form = ModificarPacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = ModificarPacienteForm(instance=paciente, initial={
            'NOMBRE': paciente.NOMBRE,
            'APELLIDOS': paciente.APELLIDOS,
            'CARNET_CI': paciente.CARNET_CI,
            'EDAD': paciente.EDAD,
            'DIRECCION': paciente.DIRECCION,
            'OCUPACION': paciente.OCUPACION,
        })
    
    context = {
        'form': form,
        'paciente': paciente,
    }
    return render(request, 'modificar_paciente.html', context)

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    context = {
        'pacientes': pacientes
    }
    return render(request, 'lista_pacientes.html', context)

def pacientes_sin_historias(request):
    pacientes = Paciente.objects.filter(historiaclinica__isnull=True)
    return render(request, 'pacientes_sin_historias.html', {'pacientes': pacientes})

def eliminar_paciente(request, id_paciente):
    paciente = get_object_or_404(Paciente, ID_PACIENTE=id_paciente)
    
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista-pacientes')
    
    context = {
        'paciente': paciente
    }
    
    return render(request, 'lista-pacientes.html', context)

def agregar_historia_clinica(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')  # Redirigir a la lista de pacientes después de agregar la historia clínica
    else:
        form = HistoriaClinicaForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'agregar_historia_clinica.html', context)


def historia_clinica(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    historia_clinica = paciente.historiaclinica_set.first()

    if not historia_clinica:
        error_message = 'El paciente no tiene una historia clínica. Por favor, cree una.'
        return JsonResponse({'error_message': error_message})

    # Resto del código de la vista
    return render(request, 'historia_clinica.html', {'paciente': paciente, 'historia_clinica': historia_clinica})

def lista_historias_clinicas(request):
    historias_clinicas = HistoriaClinica.objects.all()

    if not historias_clinicas:
        error_message = 'No se han creado historias clínicas.'
        return JsonResponse({'error_message': error_message})

    context = {
        'historias_clinicas': historias_clinicas
    }

    return render(request, 'lista_historias_clinicas.html', context)



