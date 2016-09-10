from django import forms
from .models import Consulta

class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ('fecha', 'time', 'issue')

