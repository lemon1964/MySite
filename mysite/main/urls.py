from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostsMain.as_view(), name='home_main'),  # http://127.0.0.1:8000
    path('logo/', views.logo, name='logo'),
    path('post/<slug:post_slug>/', views.ShowPostMain.as_view(), name='post_main'),
    path('add/', views.AddPostMain.as_view(), name='add_post_main'),
]



