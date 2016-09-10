from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.HomeConsultas.as_view(), name="list"),
	url(r'^nreceta/$', views.NuevaReceta.as_view(), name="newReceta"),
	url(r'^borrar/(?P<pk>\d+)/$', views.ConDelete.as_view(), name="delete"),
]