from django.contrib import admin
from .models import Paciente, Medico, Especialidad, CitaMedica, HistorialClinico, RecetaMedica

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Especialidad)
admin.site.register(CitaMedica)
admin.site.register(HistorialClinico)
admin.site.register(RecetaMedica)
