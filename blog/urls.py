from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.All_blogs, name='All_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]