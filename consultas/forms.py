from django import forms
from .models import Consulta

class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('fecha', 'time', 'nom_paciente', 'apellido_paterno', 'apellido_materno',
                'edad', 'telefono', 'correo', 'doctor', 'issue')
