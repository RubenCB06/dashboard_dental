from django.db import models
from django.contrib.auth.models import User

class Medico(models.Model):
	OPCIONES = [
    	 ('hombre','Hombre'),
    	 ('mujer','Mujer'),
    ]
	edad = models.IntegerField()
	sexo = models.CharField(max_length=140, choices=OPCIONES,default="Hombre")
	ESPECIALIAD = [
		('endodoncia', 'Endodoncia'), 
		('odontopediatria','Odontopediatría'),
		('ortodoncia', 'Ortodoncia'),
		('periodoncia', 'Periodoncia'),
		('Implantologia', 'Periodoncia'),
		('prot-bucal','Prótesis Bucal'), 
		('prot-maxilofacial','Prótesis Maxilofacial'),
		('salud-publica','Salud Pública Bucal'),
		('materiales-detales','Materiales Dentales'),
		('patoliga-bucal','Patologia Bucal'),	
    ]
	especialidad = models.CharField(max_length=140,choices=ESPECIALIAD,default="Ortodoncia")
	telefono = models.IntegerField() 
	foto = models.ImageField(upload_to='fotomedico')
	user = models.OneToOneField(User)

	def __str__(self):
		return '{} {}'.format(self.nombre,self.apellidos)
