from django.urls import path
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
	path('login/', login, name='login', kwargs={
			'template_name': 'accounts/login_form.html',
			}),
	path('logout/', logout, name='logout', kwargs={'next_page': 'login',}),
	path('signup/', views.signup, name='signup'),
	path('profile/', views.profile, name='profile'),
	]
