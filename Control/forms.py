from django import forms
from .models import HistoriaClinica, Profesional
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellidos', 'carnet_id', 'edad', 'direccion', 'ocupacion', 'carrera']

class EditarPacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellidos', 'carnet_id', 'edad', 'direccion', 'ocupacion', 'carrera']


class HistoriaClinicaForm(forms.Form):
    paciente_id = forms.ModelChoiceField(queryset=Paciente.objects.all(), label='Paciente', to_field_name='id_paciente')
    fecha_creacion = forms.DateField(label='Fecha de creación', widget=forms.DateInput(attrs={'type': 'date', 'input_format': '%Y-%m-%d'}))
    fecha_modificacion = forms.DateField(label='Fecha de modificación', widget=forms.DateInput(attrs={'type': 'date', 'input_format': '%Y-%m-%d'}))
    motivo_consulta = forms.CharField(max_length=255, label='Motivo de consulta')
    riesgo_laboral = forms.CharField(max_length=255, label='Riesgo laboral')
    ap_personal = forms.CharField(max_length=255, label='Antecedentes personales')
    ap_familiar = forms.CharField(max_length=255, label='Antecedentes familiares')
    habitos_toxicos = forms.CharField(max_length=255, label='Hábitos tóxicos')
    alergico_medic = forms.CharField(max_length=255, label='Alergias a medicamentos')
    operaciones = forms.CharField(max_length=255, label='Operaciones')
    transfusion_sangre = forms.CharField(max_length=255, label='Transfusión de sangre')
    vacunacion = forms.CharField(max_length=255, label='Vacunación')
    profesional = forms.ModelChoiceField(queryset=Profesional.objects.all(), label='Profesional')
    
# class HistoriaClinicaForm(forms.ModelForm):
#     class Meta:
#         model = HistoriaClinica
#         fields = (
#             'fecha_creacion',
#             'fecha_modificacion',
#             'motivo_consulta',
#             'riesgo_laboral',
#             'ap_personal',
#             'ap_familiar',
#             'habitos_toxicos',
#             'alergico_medic',
#             'operaciones',
#             'transfusion_sangre',
#             'vacunacion',
#             'profesional',
#         )
#         widgets = {
#             'fecha_creacion': forms.DateInput(attrs={'type': 'date', 'input_format': '%Y-%m-%d'}),
#             'fecha_modificacion': forms.DateInput(attrs={'type': 'date', 'input_format': '%Y-%m-%d'}),
#         }
        
# class ModificarHistoriaClinicaForm(forms.ModelForm):
#     class Meta:
#         model = HistoriaClinica
#         exclude = ['ID_HISTORIA', 'FECHA_CREACION', 'PACIENTE']
#         widgets = {
#             'FECHA_MODIFICACION': forms.DateInput(attrs={'type': 'date', 'input_format': '%Y-%m-%d'}),
#         }