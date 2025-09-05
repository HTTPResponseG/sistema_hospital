from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Paciente, CitaMedica, HistorialClinico, RecetaMedica
from hospital.forms import PacienteForm, CitaMedicaForm, RecetaMedicaForm, HistorialClinicoForm
from django.db.models import Q

def home(request):
    return render(request, "home/home.html")

# Listar pacientes
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "pacientes/listarPacientes.html", {"pacientes": pacientes})

# Buscar paciente por rut o nombre 
def buscar_paciente(request):
    query = request.GET.get("q")
    if query:
        pacientes = Paciente.objects.filter(
            Q(rut__iexact=query) | Q(nombre__icontains=query)
        )
    else: 
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

def buscar_cita(request):
    query = request.GET.get("q")
    if query:
        citas = CitaMedica.objects.filter(Q(fecha__icontains=query) | Q(paciente__nombre__icontains=query))
    else:
        citas = CitaMedica.objects.all()
    return render(request, 'citas/listarCitas.html', {"citas": citas})
    
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

# -------------------------------
# Historial Clinico
# -------------------------------

def listar_historiales(request):
    historiales = HistorialClinico.objects.select_related("paciente")
    return render(request, "historiales/listarHistoriales.html", {"historiales": historiales})

def ver_historial(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    historial, creado = HistorialClinico.objects.get_or_create(paciente=paciente)
    return render(request, "historiales/verHistorial.html", {
        "historial": historial,
        "paciente": paciente
    })

def crear_historial(request):
    if request.method == "POST":
        form = HistorialClinicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_historiales")
    else:
        form = HistorialClinicoForm()
    return render(request, "historiales/crearHistorial.html", {"form": form})

# -------------------------------
# Receta Medica
# -------------------------------

def listar_recetas(request):
    recetas = RecetaMedica.objects.select_related("cita", "cita__paciente", "cita__medico")
    return render(request, "recetas/listarRecetas.html", {"recetas": recetas})

def ver_recetas(request, cita_id):
    cita = get_object_or_404(CitaMedica, id=cita_id)
    recetas = RecetaMedica.objects.filter(cita=cita)
    return render(request, "recetas/verRecetas.html", {"recetas": recetas, "cita": cita})

def crear_receta(request):
    if request.method == "POST":
        form = RecetaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_recetas")
    else:
        form = RecetaMedicaForm()
    return render(request, "recetas/crearReceta.html", {"form": form})



# Devolver JSON sin DRF
def citas_json(request):
    citas = list(CitaMedica.objects.values("fecha", "motivo", "paciente__nombre", "medico__nombre"))
    return JsonResponse({"citas": citas})


