from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name='index'),
    path('<pk>', views.post_detail, name='post_detail'),
	path('<post_pk>/comment/new/', views.comment_new, name='comment_new'),
	path('<post_pk>/comment/<pk>/edit/', views.comment_edit, name='comment_edit'),
	path('<post_pk>/comment/<pk>/delete/', views.comment_delete, name='comment_delete'),
]
