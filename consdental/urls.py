from django.conf.urls import url,include
from django.contrib import admin
from consultas import urls as consultasUrls
from django.views.static import serve
from django.conf import settings
from consultas import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^consulta/',include(consultasUrls)),
    url(
    	regex=r'^media/(?P<path>.*)/$',
    	view=serve,
    	kwargs={"document_root":settings.MEDIA_ROOT}
    	)
]
