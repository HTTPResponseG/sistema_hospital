from django import forms
from .models import Paciente, Medico, CitaMedica

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
