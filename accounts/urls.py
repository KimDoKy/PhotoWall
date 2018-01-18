from django.urls import path
from django.contrib.auth.views import login

urlpatterns = [
	path('login/', login, name='login', kwargs={
			'template_name': 'accounts/login_form.html',
			}),
	]
