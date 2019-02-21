from django.conf.urls import url
from . import views 

app_name='app'
url=[
	
	url(r'^index/', views.base, name='base')
	
]