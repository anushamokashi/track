from django.conf.urls import urls

from . import views
app_name='authentication'

urls= [

	url(r'^login/', views.login, name='login'),
	url(r'^signup/', views.signup, name='signup'),

]