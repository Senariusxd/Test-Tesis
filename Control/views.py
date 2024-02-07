from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Paciente , HistoriaClinica
from .forms import PacienteForm, EditarPacienteForm, HistoriaClinicaForm

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







def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})


def agregar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    
    return render(request, 'agregar_paciente.html', {'form': form})

def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    
    if request.method == 'POST':
        form = EditarPacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = EditarPacienteForm(instance=paciente)
    
    return render(request, 'editar_paciente.html', {'form': form, 'paciente': paciente})

def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id_paciente=paciente_id)
    
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    
    return render(request, 'eliminar_paciente.html', {'paciente': paciente})


def lista_historias_clinicas(request):
    historias_clinicas = HistoriaClinica.objects.all()
    
    return render(request, 'lista_historias_clinicas.html', {'historias_clinicas': historias_clinicas})

def crear_historia_clinica(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            paciente = form.cleaned_data['paciente_id']
            historia_clinica = HistoriaClinica(paciente=paciente)
            historia_clinica.fecha_creacion = form.cleaned_data['fecha_creacion']
            historia_clinica.fecha_modificacion = form.cleaned_data['fecha_modificacion']
            historia_clinica.motivo_consulta = form.cleaned_data['motivo_consulta']
            historia_clinica.riesgo_laboral = form.cleaned_data['riesgo_laboral']
            historia_clinica.ap_personal = form.cleaned_data['ap_personal']
            historia_clinica.ap_familiar = form.cleaned_data['ap_familiar']
            historia_clinica.habitos_toxicos = form.cleaned_data['habitos_toxicos']
            historia_clinica.alergico_medic = form.cleaned_data['alergico_medic']
            historia_clinica.operaciones = form.cleaned_data['operaciones']
            historia_clinica.transfusion_sangre = form.cleaned_data['transfusion_sangre']
            historia_clinica.vacunacion = form.cleaned_data['vacunacion']
            historia_clinica.profesional = form.cleaned_data['profesional']
            # Completa con los campos restantes de la historia clínica
            historia_clinica.save()
            return redirect('lista_historias_clinicas')
    else:
        form = HistoriaClinicaForm()
    
    return render(request, 'crear_historia_clinica.html', {'form': form})

def eliminar_historia_clinica(request, historia_id):
    historia = get_object_or_404(HistoriaClinica, paciente_id=historia_id)
    historia.delete()
    return redirect('lista_historias')

def modificar_historia_clinica(request, historia_id):
    historia_clinica = get_object_or_404(HistoriaClinica, pk=historia_id)

    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            historia_clinica.paciente = form.cleaned_data['paciente_id']
            historia_clinica.fecha_creacion = form.cleaned_data['fecha_creacion']
            historia_clinica.fecha_modificacion = form.cleaned_data['fecha_modificacion']
            historia_clinica.motivo_consulta = form.cleaned_data['motivo_consulta']
            historia_clinica.riesgo_laboral = form.cleaned_data['riesgo_laboral']
            historia_clinica.ap_personal = form.cleaned_data['ap_personal']
            historia_clinica.ap_familiar = form.cleaned_data['ap_familiar']
            historia_clinica.habitos_toxicos = form.cleaned_data['habitos_toxicos']
            historia_clinica.alergico_medic = form.cleaned_data['alergico_medic']
            historia_clinica.operaciones = form.cleaned_data['operaciones']
            historia_clinica.transfusion_sangre = form.cleaned_data['transfusion_sangre']
            historia_clinica.vacunacion = form.cleaned_data['vacunacion']
            historia_clinica.profesional = form.cleaned_data['profesional']
            # Completa con los campos restantes de la historia clínica
            historia_clinica.save()
            return redirect('lista_historias_clinicas')
    else:
        form = HistoriaClinicaForm(initial={
            'paciente_id': historia_clinica.paciente,
            'fecha_creacion': historia_clinica.fecha_creacion,
            'fecha_modificacion': historia_clinica.fecha_modificacion,
            'motivo_consulta': historia_clinica.motivo_consulta,
            'riesgo_laboral': historia_clinica.riesgo_laboral,
            'ap_personal': historia_clinica.ap_personal,
            'ap_familiar': historia_clinica.ap_familiar,
            'habitos_toxicos': historia_clinica.habitos_toxicos,
            'alergico_medic': historia_clinica.alergico_medic,
            'operaciones': historia_clinica.operaciones,
            'transfusion_sangre': historia_clinica.transfusion_sangre,
            'vacunacion': historia_clinica.vacunacion,
            'profesional': historia_clinica.profesional,
            # Completa con los campos restantes del formulario
        })
    
    return render(request, 'modificar_historia_clinica.html', {'form': form})

def eliminar_historia_clinica(request, historia_id):
    historia = get_object_or_404(HistoriaClinica, pk=historia_id)
    historia.delete()
    return redirect('lista_historias_clinicas')

def ver_historia_clinica(request, historia_id):
    historia_clinica = get_object_or_404(HistoriaClinica, pk=historia_id)
    return render(request, 'ver_historia_clinica.html', {'historia_clinica': historia_clinica})