from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomeMedicos.as_view(), name="list"),
	url(r'^nueva/$', views.NuevaConsulta.as_view(), name="newconsulta"),
	
]