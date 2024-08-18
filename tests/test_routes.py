import unittest
from app import create_app, db
from app.models import Appointment
from datetime import datetime

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_appointment(self):
        response = self.client.post('/appointments', json={
            'patient_name': 'John Doe',
            'doctor_name': 'Dr. Smith',
            'appointment_time': '2024-08-01T10:00:00',
            'description': 'Routine checkup'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_appointments(self):
        with self.app.app_context():
            appointment = Appointment(
                patient_name="John Doe",
                doctor_name="Dr. Smith",
                appointment_time=datetime(2024, 8, 1, 10, 0, 0),
                description="Routine checkup"
            )
            db.session.add(appointment)
            db.session.commit()

        response = self.client.get('/appointments')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
