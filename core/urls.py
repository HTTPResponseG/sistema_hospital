
from django.contrib import admin
from django.urls import path
from hospital import views

urlpatterns = [
    path("", views.home, name="home"),
    path('admin/', admin.site.urls, name="admin"),

    #Pacientes
    path("pacientes/", views.listar_pacientes, name="listar_pacientes"),
    path("pacientes/nuevo/", views.crear_paciente, name="crear_paciente"),
    path('pacientes/buscar/', views.buscar_paciente, name='buscar_paciente'),

    #Citas
    path("citas/", views.listar_citas, name="listar_citas"),
    path("citas/nueva/", views.crear_cita, name="crear_cita"),
    path("citas/buscar/", views.buscar_cita, name="buscar_cita"),
    path("citas/json/", views.citas_json, name="citas_json"),

    # Historiales
    path("historiales/", views.listar_historiales, name="listar_historiales"),
    path("historial/<int:paciente_id>/", views.ver_historial, name="ver_historial"),
    path("historial/nuevo/", views.crear_historial, name="crear_historial"),

    # Recetas
    path("recetas/", views.listar_recetas, name="listar_recetas"),
    path("recetas/<int:cita_id>/", views.ver_recetas, name="ver_recetas"),
    path("recetas/nueva/", views.crear_receta, name="crear_receta"),

]
