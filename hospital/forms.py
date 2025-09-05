from django import forms
from .models import Paciente, Medico, CitaMedica, HistorialClinico, RecetaMedica

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["rut", "nombre", "fecha_nacimiento"]

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ["nombre", "especialidad", "correo"]

class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ["fecha", "motivo", "paciente", "medico", "especialidad"]

class HistorialClinicoForm(forms.ModelForm):
    class Meta:
        model = HistorialClinico
        fields = ["paciente", "antecedentes", "alergias", "enfermedades_cronicas"]

class RecetaMedicaForm(forms.ModelForm):
    class Meta:
        model = RecetaMedica
        fields = ["cita", "medicamento", "dosis", "indicaciones"]

