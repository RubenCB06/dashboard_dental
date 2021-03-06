from django.conf.urls import url
from . import views
from django.contrib.auth import views as djangoViews

urlpatterns = [
	url(r'^accounts/profile/$', views.PerfilView.as_view(), name="perfil"),
	url(r'^login/$', djangoViews.login, name="login"),
	url(r'^logout/$', djangoViews.logout, name="logout"),
	#url(r'^alta/$', views.Alta.as_view(), name="alta"),
]