from django.conf.urls import url,include
from django.contrib import admin
from consultas import urls as consultasUrls
from medico import urls as medicoUrls
from paciente import urls as pacienteUrls
from django.views.static import serve
from django.conf import settings
from consultas import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^consulta/',include(consultasUrls)),
	url(r'^medico/',include(medicoUrls)),
	url(r'^paciente/',include(pacienteUrls)),
	url(r'^nuevopaciente', views.NuevoPaciente.as_view(),),
    url(
    	regex=r'^media/(?P<path>.*)/$',
    	view=serve,
    	kwargs={"document_root":settings.MEDIA_ROOT}
    	)
]
