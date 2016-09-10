from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomePaciente.as_view(), name="list"),
	
]