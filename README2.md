# Citas API

## Descripción
Esta es una API para gestionar citas médicas. Permite crear, leer, actualizar y eliminar citas.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio. 
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   flask db upgrade
   flask run

## Uso de la API
Crear una nueva cita
Endpoint: /appointments
Método: POST
Ejemplo de solicitud:
curl -X POST http://127.0.0.1:5000/appointments -H "Content-Type: application/json" -d '{"patient_name": "John Doe", "doctor_name": "Dr. Smith", "appointment_time": "2024-08-01T10:00:00", "description": "Routine checkup"}'

## Obtener todas las citas
Endpoint: /appointments
Método: GET
Pruebas
Para ejecutar las pruebas, utiliza el siguiente comando:
    pytest








   





