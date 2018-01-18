from django.urls import path
from django.contrib.auth.views import login
from . import views

urlpatterns = [
	path('login/', login, name='login', kwargs={
			'template_name': 'accounts/login_form.html',
			}),
	path('signup/', views.signup, name='signup'),
	]
