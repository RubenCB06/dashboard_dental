from django.db import models

class Medico(models.Model):
	OPCIONES = [
    	 ('hombre','Hombre'),
    	 ('mujer','Mujer'),
    ]
	nombre = models.CharField(max_length=140)
	apellidos = models.CharField(max_length=140)
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
	correo = models.EmailField(max_length=100)
	foto = models.ImageField(upload_to='fotomedico')

	def __str__(self):
		return '{} {}'.format(self.nombre,self.apellidos)