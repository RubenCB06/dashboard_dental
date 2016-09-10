
from accounts.models import Medico
from django.shortcuts import render
from .forms import NewConsultaForm
from django.views.generic import ListView, View, DeleteView
from .models import Consulta
from django.utils.text import slugify
from django.core.urlresolvers import reverse_lazy



class HomeMedicos(ListView):
	model = Medico
	queryset = model.objects.all().order_by('id')
	template_name = 'consultas/medico_list.html'
		
class NuevaConsulta(View):
	def get(self, request):
		template_name = 'consultas/nuevoconsulta.html'
		form = NewConsultaForm()
		context ={
		'form':form,
		}
		return render(request, template_name, context)
	
	def post(self, request):
		form = NewConsultaForm(request.POST,request.FILES)
		if form.is_valid():
			nuevo_consulta = form.save(commit=True)
			nuevo_consulta.save()
		else:
			context = {
			'form':form,
			}
			template_name = 'consultas/nuevoconsulta.html'
			return render(request, template_name, context)
			success_url = reverse_lazy('list')


class ConDelete(DeleteView):
	model = Consulta 
	success_url = reverse_lazy('home')