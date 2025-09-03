from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Paciente, Medico, Especialidad, CitaMedica
from hospital.forms import PacienteForm, MedicoForm, CitaMedicaForm


def home(request):
    return render(request, "home/home.html")

# Listar pacientes
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/listarPacientes.html", {"pacientes": pacientes})

# Crear paciente
def crear_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_pacientes")
    else:
        form = PacienteForm()
    return render(request, "pacientes/crearPaciente.html", {"form": form})

# Listar citas médicas
def listar_citas(request):
    citas = CitaMedica.objects.select_related("paciente", "medico", "especialidad")
    return render(request, "citas/listarCitas.html", {"citas": citas})

# Crear cita
def crear_cita(request):
    if request.method == "POST":
        form = CitaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_citas")
    else:
        form = CitaMedicaForm()
    return render(request, "citas/crearCita.html", {"form": form})

# Devolver JSON sin DRF
def citas_json(request):
    citas = list(CitaMedica.objects.values("fecha", "motivo", "paciente__nombre", "medico__nombre"))
    return JsonResponse({"citas": citas})


