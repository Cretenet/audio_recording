from django.urls import path
from . import views

urlpatterns = [
    path('recording_page/', views.recording_page),
    path('upload_audio/', views.upload_audio),
    path('go_to/', views.go_to),
    path('check_pass/', views.check_pass), 
    path('failure/', views.failure)
]