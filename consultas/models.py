from django.db import models
from accounts.models import Medico

	

class Consulta(models.Model):
	fecha = models.DateField(auto_now=False)
	time = models.TimeField(auto_now=False)
	nom_paciente = models.CharField(max_length = 50, null=True, blank=True)
	edad = models.IntegerField()
	telefono = models.IntegerField(null=False, blank=False)
	correo = models.CharField(max_length = 50, null=False, blank=False)
	doctor = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='doctor')
	issue = models.TextField()

	def __str__(self):
		return 'El dia {} con doctor {} con el paciente {}'.format(self.fecha,self.doctor,self.nom_paciente)