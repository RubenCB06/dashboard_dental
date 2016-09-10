from django import forms
from .models import Paciente, Medico, Consulta

class NewPatientForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = ('nombre', 'apellidos', 'edad', 'sexo', 'telefono', 'correo')

