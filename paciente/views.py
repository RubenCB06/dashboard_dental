from django.views.generic import ListView
from .models import Paciente
from django.shortcuts import render

class HomePaciente(ListView):
	model = Paciente
	queryset = model.objects.all().order_by('id')
	template_name = 'consultas/medico_list.html'
