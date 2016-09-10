from django import forms
from .models import Paciente, Medico, Consulta

class NewPatientForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = ('nombre', 'apellidos', 'edad', 'sexo', 'telefono', 'correo')

class NewDoctorForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nombre', 'apellidos', 'edad', 'sexo', 'especialidad', 'telefono', 'correo', 'foto')

class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('fecha', 'time', 'issue')

