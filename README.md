🏥 Sistema de Gestión de Citas Médicas

Este proyecto es un sistema web desarrollado en Django que permite gestionar pacientes, médicos, especialidades, citas médicas, recetas y el historial clínico de cada paciente.
El sistema busca simular cómo se organiza la información en un hospital, integrando relaciones entre entidades y una interfaz intuitiva con Bootstrap, conectada a una base de datos MySQL.

✨ Funcionalidades principales

👨‍⚕️ Gestión de pacientes: crear, listar y buscar pacientes.

📅 Gestión de citas médicas: agendar, listar y visualizar citas con médicos y especialidades asociadas.

💊 Gestión de recetas médicas: registrar medicamentos, dosis e indicaciones vinculadas a una cita específica.

📝 Historial clínico del paciente: almacenar antecedentes, alergias y enfermedades crónicas.

🛠️ Panel de administración de Django: gestión avanzada de todas las entidades del sistema.

🔗 Navegación fluida con Bootstrap: interfaz amigable y moderna.

💾 Integración con base de datos MySQL.


🗂️ Modelo Entidad-Relación (MER)

El sistema está compuesto por las siguientes entidades principales:

Paciente 🧑‍⚕️: contiene los datos personales de cada paciente (RUT, nombre y fecha de nacimiento).

Médico 👨‍⚕️: almacena los datos del médico, incluyendo nombre, correo y su especialidad.

Especialidad 🩺: define las diferentes áreas médicas (ejemplo: cardiología, pediatría, endocrinología).

Cita Médica 📅: representa una cita agendada entre un paciente y un médico en una especialidad determinada.

Receta Médica 💊: vinculada a una cita, permite registrar medicamentos, dosis e indicaciones.

Historial Clínico 📋: asociado al paciente, registra antecedentes, alergias y enfermedades crónicas.


🔗 Relaciones

Un paciente puede tener muchas citas médicas.

Un médico puede atender en muchas citas médicas.

Una especialidad puede estar asociada a muchos médicos y a muchas citas médicas.

Cada cita médica se relaciona únicamente con un paciente, un médico y una especialidad.

Una cita puede tener muchas recetas; cada receta pertenece a una cita.

Cada paciente puede tener como máximo un historial clínico (puede no tenerlo); cada historial pertenece a un paciente.


🛠️ Tecnologías utilizadas
Python 3.x
Django 5.x
HTML + Bootstrap 5
Base de datos MySQL (puede usarse SQLite por defecto para desarrollo rápido)

🚀 Instalación y ejecución
Sigue estos pasos para clonar y ejecutar el proyecto en tu entorno local:

1️⃣ Clonar el repositorio:
git clone https://github.com/HTTPResponseG/sistema_hospital.git
cd sistema_hospital

2️⃣ Crear y activar un entorno virtual

En Linux / Mac:
python3 -m venv venv

source venv/bin/activate

En Windows (PowerShell):
python -m venv venv

venv\Scripts\activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Configurar base de datos
Por defecto, el proyecto está configurado para MySQL.
Si deseas usar SQLite (más sencillo para pruebas), edita el archivo settings.py y reemplaza la sección de DATABASES por:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

5️⃣ Ejecutar migraciones

python manage.py makemigrations

python manage.py migrate

6️⃣ Crear superusuario (para acceder al panel de administración)
python manage.py createsuperuser

7️⃣ Levantar el servidor

python manage.py runserver

Luego abre en el navegador:
http://127.0.0.1:8000/
 → Página principal del sistema.

http://127.0.0.1:8000/admin/
 → Panel de administración de Django.


