
from django.contrib import admin
from django.urls import path
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("pacientes/", views.listar_pacientes, name="listar_pacientes"),
    path("pacientes/nuevo/", views.crear_paciente, name="crear_paciente"),
    path("citas/", views.listar_citas, name="listar_citas"),
    path("citas/nueva/", views.crear_cita, name="crear_cita"),
    path("citas/json/", views.citas_json, name="citas_json"),
]
