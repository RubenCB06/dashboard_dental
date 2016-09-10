from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomeConsultas.as_view(), name="list"),
	
]