from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Consulta
from django.utils.text import slugify
#from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeConsultas(ListView):
	model = Consulta
	queryset = model.objects.all().order_by('id')
	template_name = 'consultas/medico_list.html'
		
'''class NuevoPaciente(View):
	#@method_decorator(login_required)
	def get(self, request):
		template_name = 'consultas/nuevopaciente.html'
		form = NewPatientForm()
		context ={
		'form':form,
		}
		return render(request, template_name, context)
	
	def patient(self, request):
		form = NewPostForm(request.POST,request.FILES)
		if form.is_valid():
			nuevo_paciente = form.save(commit=False)
			nuevo_paciente.slug = slugify(nuevo_paciente.nombre)
			nuevo_paciente.save()
		else:
			context = {
			'form':form,
			}
			template_name = 'consultas/nuevopaciente.html'
			return render(request, template_name, context)
'''