from django import forms
from .models import Consulta

class NewConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('fecha', 'time', 'nom_paciente', 'apellido_paterno', 'apellido_materno',
                'edad', 'telefono', 'correo', 'doctor', 'issue')
        labels = {'fecha' : 'Fecha', 'time' : 'Hora', 'nom_paciente' : 'Nombre', 
                  'apellido_paterno' : 'Apellido Paterno' , 'apellido_materno' : 'Apellido Materno',
                  'edad' : 'Edad' , 'telefono' : 'Teléfono' , 'correo' : 'Correo', 
                  'doctor' : 'Doctor' , 'issue' : "Descripción" }