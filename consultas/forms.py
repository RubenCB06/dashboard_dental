from django import forms
from .models import Consulta

class NewConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('fecha', 'time', 'nom_paciente', 'edad', 'telefono', 'correo', 'doctor', 'issue')
        labels = {'fecha' : 'Fecha', 'time' : 'Hora', 'nom_paciente' : 'Nombre', 
                  'edad' : 'Edad' , 'telefono' : 'Teléfono' , 'correo' : 'Correo', 
                  'doctor' : 'Doctor' , 'issue' : "Descripción" }
        widgets = {
			'fecha' : forms.TextInput(attrs={'class':'form-control','placeholder':'Fecha'}),
			'time' : forms.TimeInput(attrs={'class':'form-control','placeholder':'Hora'}),
			'nom_paciente' : forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre Completo'}),
			'edad' : forms.TextInput(attrs={'class':'form-control','placeholder':'Edad'}) , 
			'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}) ,
			'correo':forms.TextInput(attrs={'class':'form-control','placeholder':'Correo'}) ,
			'doctor':forms.Select(attrs={'class':'form-control','placeholder':'Doctor'}),
			'issue' :forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción del Problema:'}),

		}