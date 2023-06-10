from django.urls import path
from . import views

urlpatterns = [
    path('recording_page/', views.recording_page, name='recording_page'),
    path('upload_audio/', views.upload_audio, name='upload_audio'),
    path('go_to/', views.go_to, name='go_to'),
    path('login/', views.login, name='login'),
    path('audio_list/', views.audio_list, name='audio_list'),
    path('download_all/', views.download_all, name='download_all')
]