from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Paciente , HistoriaClinica
from .forms import PacienteForm, HistoriaClinicaForm

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

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    context = {
        'pacientes': pacientes
    }
    return render(request, 'lista_pacientes.html', context)

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


#Listar las Historias Clinicas
from django.shortcuts import render, get_object_or_404
from .models import Paciente

def historia_clinica(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    historia_clinica = paciente.historiaclinica_set.first()

    if not historia_clinica:
        error_message = 'El paciente no tiene una historia clínica. Por favor, cree una.'
        return JsonResponse({'error_message': error_message})

    # Resto del código de la vista
    return render(request, 'historia_clinica.html', {'paciente': paciente, 'historia_clinica': historia_clinica})


def todas_historias_clinicas(request):
    historias_clinicas = HistoriaClinica.objects.all()
    return render(request, 'todas_historias_clinicas.html', {'historias_clinicas': historias_clinicas})