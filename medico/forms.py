from django import forms
from .models import Paciente, Medico, Consulta

class NewDoctorForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('nombre', 'apellidos', 'edad', 'sexo', 'especialidad', 'telefono', 'correo', 'foto')
