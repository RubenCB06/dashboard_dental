from django.db import models
from django.contrib.auth.models import User

class Medico(models.Model):
	OPCIONES = [
    	 ('hombre','Hombre'),
    	 ('mujer','Mujer'),
    ]
	nombre = models.CharField(max_length = 50, null=True, blank=True)
	apellido_materno = models.CharField(max_length = 50, null=True, blank=True)
	apellido_paterno = models.CharField(max_length = 50, null=True, blank=True)
	edad = models.IntegerField()
	sexo = models.CharField(max_length=140, choices=OPCIONES,default="Hombre")
	ESPECIALIAD = [
		('Endodoncia', 'Endodoncia'), 
		('Odontopediatría','Odontopediatría'),
		('Ortodoncia', 'Ortodoncia'),
		('Periodoncia', 'Periodoncia'),
		('Implantología', 'Implantología'),
		('Prótesis Bucal','Prótesis Bucal'), 
		('Prótesis Maxilofacial','Prótesis Maxilofacial'),
		('Salud Pública Bucal','Salud Pública Bucal'),
		('Materiales Dentales','Materiales Dentales'),
		('Patologia Bucal','Patologia Bucal'),	
    ]
	email = models.CharField(max_length = 50, null=True, blank=True)
	especialidad = models.CharField(max_length=140,choices=ESPECIALIAD,default="Ortodoncia")
	telefono = models.IntegerField() 
	foto = models.ImageField(upload_to='fotomedico')
	descripcion = models.TextField(blank=True,null=True)
	user = models.OneToOneField(User)

	def __str__(self):
		return '{} {} - {}'.format(self.nombre, self.apellido_paterno, self.especialidad)
