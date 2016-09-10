from django.views.generic import ListView
from .models import Medico
from django.shortcuts import render

class HomeMedico(ListView):
	model = Medico
	queryset = model.objects.all().order_by('id')
	template_name = 'consultas/medico_list.html'