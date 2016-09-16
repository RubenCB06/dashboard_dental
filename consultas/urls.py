from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.HomeMedicos.as_view(), name="home"),
	url(r'^nuevaconsulta/$', views.NuevaConsulta.as_view(), name="newconsulta"),
	url(r'^borrarconsulta/(?P<pk>\d+)/$', views.ConDelete.as_view(), name="delete"),
	url(r'^editar/(?P<pk>\d+)/$', views.ConsultaUpdate.as_view(), name="update"),

]