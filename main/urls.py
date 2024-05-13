from . import views
from django.urls import path, include


app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('foto.html', views.photo, name = 'foto'),
    path('index.html', views.index, name = 'index'),
    path('video.html', views.video, name = 'video'),
    path('upload_image/', views.upload_image, name='upload_image'),
]