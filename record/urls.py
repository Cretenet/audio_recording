from django.urls import path
from . import views

urlpatterns = [
    path('recording_page/', views.recording_page),
    path('upload_audio/', views.upload_audio),
]