from django.conf.urls import url,include
from django.contrib import admin
from consultas import urls as consultasUrls
from accounts import urls as cuentasUrls
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^consultas/',include(consultasUrls)),
	url(r'^accounts/',include(cuentasUrls)),
    url(
    	regex=r'^media/(?P<path>.*)/$',
    	view=serve,
    	kwargs={"document_root":settings.MEDIA_ROOT}
    	)
]
