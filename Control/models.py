from django.db import models

class Profesional(models.Model):
    id_profesional = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    carnet_id = models.IntegerField()

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    carnet_id = models.IntegerField()
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    OCUPACIONES_CHOICES = (
        ('estudiante', 'Estudiante'),
        ('trabajador', 'Trabajador'),
    )
    ocupacion = models.CharField(max_length=255, choices=OCUPACIONES_CHOICES)
    CARRERAS_CHOICES = (
        ('ing-informatico', 'Ing. Informático'),
        ('ing-mecanico', 'Ing. Mecánico'),
        ('ing-industrial', 'Ing. Industrial'),
        ('ing-quimico', 'Ing. Químico'),
        ('ing-agronomo', 'Ing. Agrónomo'),
        ('lic-contabilidad', 'Lic. Contabilidad'),
        ('lic-economia', 'Lic. Economía'),
        ('lic-derecho', 'Lic. Derecho'),
        ('lic-cultura-fisica', 'Lic. Cultura Física'),
        ('lic-estudios-socioculturales', 'Lic. Estudios Socioculturales'),
    )
    carrera = models.CharField(max_length=255, choices=CARRERAS_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.ocupacion != 'estudiante':
            self.carrera = ""
        super().save(*args, **kwargs)


class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, primary_key=True)
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    motivo_consulta = models.CharField(max_length=255)
    riesgo_laboral = models.CharField(max_length=255)
    ap_personal = models.CharField(max_length=255)
    ap_familiar = models.CharField(max_length=255)
    habitos_toxicos = models.CharField(max_length=255)
    alergico_medic = models.CharField(max_length=255)
    operaciones = models.CharField(max_length=255)
    transfusion_sangre = models.CharField(max_length=255)
    vacunacion = models.CharField(max_length=255)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.paciente)

    


    
    