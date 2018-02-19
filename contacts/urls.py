from django.conf.urls import url

from . import views
from django.contrib.auth import views as loginviews

urlpatterns = [
	url(r'^$', loginviews.login,name="login"),
	url(r'^accounts/profile/$', views.redirecting,name="redirecting"),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^home/$',views.view_home,name="view_home")
]