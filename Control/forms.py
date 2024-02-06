from django import forms
from .models import HistoriaClinica
from .models import Paciente

class PacienteForm(forms.ModelForm):
    OCUPACION_CHOICES = [
        ('Trabajador', 'Trabajador'),
        ('Estudiante-Ing-Informatico', 'Estudiante-Ing-Informatico'),
        ('Estudiante-Ing-Mecanico', 'Estudiante-Ing-Mecanico'),
        ('Estudiante-Ing-Industrial', 'Estudiante-Ing-Industrial'),
        ('Estudiante-Ing-Quimico', 'Estudiante-Ing-Quimico'),
        ('Estudiante-Ing-Agronoma', 'Estudiante-Ing-Agronoma'),
        ('Estudiante-Lic-Contabilidad y Finanzas', 'Estudiante-Lic-Contabilidad y Finanzas'),
        ('Estudiante-Lic-Economía', 'Estudiante-Lic-Economía'),
        ('Estudiante-Lic-Derecho', 'Estudiante-Lic-Derecho'),
        ('Estudiante-Lic-Cultura Física', 'Estudiante-Lic-Cultura Física'),
        ('Estudiante-Lic-Estudios Socioculturales', 'Estudiante-Lic-Estudios Socioculturales'),


    ]

    OCUPACION = forms.ChoiceField(choices=OCUPACION_CHOICES)

    class Meta:
        model = Paciente
        fields = ['ID_PACIENTE', 'NOMBRE', 'APELLIDOS', 'CARNET_CI', 'EDAD', 'DIRECCION', 'OCUPACION']


class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = (
            'ID_HISTORIA',
            'FECHA_CREACION',
            'FECHA_MODIFICACION',
            'MOTIVO_CONSULTA',
            'RIESGO_LABORAL',
            'AP_PERSONAL',
            'AP_FAMILIAR',
            'HABITOS_TOXICOS',
            'ALERGICO_MEDIC',
            'OPERACIONES',
            'TRANSFUCION_SANGRE',
            'VACUNACION',
            'PACIENTE',
            'PROFESIONAL',
        )
        widgets = {
            'FECHA_CREACION': forms.DateInput(attrs={'type': 'date', 'input_format': '%Y-%m-%d'}),
            'FECHA_MODIFICACION': forms.DateInput(attrs={'type': 'date', 'input_format': '%Y-%m-%d'}),
        }