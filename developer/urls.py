from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('direction/<slug:dir_slug>/', views.show_direction, name='direction'),
    path('posts/<slug:post_slug>/', views.show_post, name='posting'),
]