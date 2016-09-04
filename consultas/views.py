from django.views.generic import ListView
from .models import Medico



class Home(ListView):
	model = Medico
	queryset = model.objects.all().order_by('id')
	template_name = 'consultas/medico_list.html'
