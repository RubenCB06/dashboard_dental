from django.db import models
from accounts.models import Medico

	

class Consulta(models.Model):
	fecha = models.DateField(auto_now=False)
	time = models.TimeField(auto_now=False)
	nom_paciente = models.TextField()
	apellido_paciente = models.TextField()
	edad = models.IntegerField()
	telefono = models.IntegerField()
	correo = models.TextField()
	doctor = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='doctor')
	issue = models.TextField()

	def __str__(self):
		return 'El dia {} con doctor {} con el paciente {}'.format(self.nombre,self.apellidos,self.doctor)