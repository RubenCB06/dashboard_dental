from django.db import models

class Paciente(models.Model):
	OPCIONES = [
    	 ('hombre','Hombre'),
    	 ('mujer','Mujer'),
    ]
	nombre = models.CharField(max_length=140)
	apellidos = models.CharField(max_length=140)
	edad = models.IntegerField()
	sexo = models.CharField(max_length=140, choices=OPCIONES,default="Hombre")
	telefono = models.IntegerField() 
	correo = models.EmailField(max_length=100)
	

	def __str__(self):
		return '{} {}'.format(self.nombre,self.apellidos)