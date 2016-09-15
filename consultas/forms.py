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
        widgets = {
			'fecha' : forms.TextInput(attrs={'class':'form-control'}),
			'time' : forms.TextInput(attrs={'class':'form-control'}),
			'nom_paciente' : forms.Select(attrs={'class':'form-control'}),
			'apellido_paterno' : forms.TextInput(attrs={'class':'form-control'}),
			'apellido_materno' : forms.TextInput(attrs={'class':'form-control'}) ,
			'edad' : forms.TextInput(attrs={'class':'form-control'}) , 
			'telefono':forms.TextInput(attrs={'class':'form-control'}) ,
			'correo':forms.TextInput(attrs={'class':'form-control'}) ,
			'doctor':forms.Select(attrs={'class':'form-control'}),
			'issue' :forms.Textarea(attrs={'class':'form-control'}),

		}