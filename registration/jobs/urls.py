# jobs/urls.py
from django.urls import path
from .views import job_application

urlpatterns = [
    path('apply/', job_application, name='job_application'),   
]
