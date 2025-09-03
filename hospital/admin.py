from django.contrib import admin
from .models import Paciente, Medico, Especialidad, CitaMedica

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Especialidad)
admin.site.register(CitaMedica)

