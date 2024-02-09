# jobs/urls.py
from django.urls import path
from .views import job_application
from .views import job_list, job_detail,apply_job

urlpatterns = [
    path('apply/', job_application, name='job_application'), 
    path('job_list/', job_list, name='job_list'),
    path('job_detail/<int:id>/', job_detail, name='job_detail'),
    path('/apply_job/', apply_job, name='apply_job'),    
]
