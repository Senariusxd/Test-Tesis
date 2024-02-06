from django.db import models

class Paciente(models.Model):
    ID_PACIENTE = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=255)
    APELLIDOS = models.CharField(max_length=255)
    CARNET_CI = models.CharField(max_length=255)
    EDAD = models.CharField(max_length=255)
    DIRECCION = models.CharField(max_length=255)
    OCUPACION = models.CharField(max_length=255)
    def __str__(self):
        return self.NOMBRE
    
    

class Profesional(models.Model):
    ID_PROFESIONAL = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=255)
    APELLIDOS = models.CharField(max_length=255)
    CARNET_CI = models.CharField(max_length=255)
    def __str__(self):
        return self.NOMBRE

class HistoriaClinica(models.Model):
    ID_HISTORIA = models.IntegerField(primary_key=True)
    FECHA_CREACION = models.DateField()
    FECHA_MODIFICACION = models.DateField()
    MOTIVO_CONSULTA = models.CharField(max_length=255)
    RIESGO_LABORAL = models.CharField(max_length=255)
    AP_PERSONAL = models.CharField(max_length=255)
    AP_FAMILIAR = models.CharField(max_length=255)
    HABITOS_TOXICOS = models.CharField(max_length=255)
    ALERGICO_MEDIC = models.CharField(max_length=255)
    OPERACIONES = models.CharField(max_length=255)
    TRANSFUCION_SANGRE = models.CharField(max_length=255)
    VACUNACION = models.CharField(max_length=255)
    PACIENTE = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    PROFESIONAL = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.PACIENTE