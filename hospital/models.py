from django.db import models

# Create your models here.

class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.ForeignKey("Especialidad",
                                     on_delete=models.CASCADE)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.especialidad}"

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Paciente(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.rut}"


class CitaMedica(models.Model):
    fecha = models.DateField()
    motivo = models.CharField(max_length=100)
    paciente = models.ForeignKey("Paciente", 
                                 on_delete=models.CASCADE)
    medico = models.ForeignKey("Medico",
                               on_delete=models.CASCADE)
    especialidad = models.ForeignKey("Especialidad", 
                                     on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Cita: {self.fecha} - Paciente: {self.paciente.nombre} con Medico: {self.medico.nombre}"
