import unittest
from app.models import Appointment
from datetime import datetime

class TestModels(unittest.TestCase):

    def test_create_appointment(self):
        appointment = Appointment(
            patient_name="John Doe",
            doctor_name="Dr. Smith",
            appointment_time=datetime(2024, 8, 1, 10, 0, 0),
            description="Routine checkup"
        )
        self.assertEqual(appointment.patient_name, "John Doe")
        self.assertEqual(appointment.doctor_name, "Dr. Smith")
        self.assertEqual(appointment.description, "Routine checkup")

if __name__ == '__main__':
    unittest.main()
