from django.db import models

class Candidate(models.Model):
    job_title = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50)
    company_email = models.EmailField(default='example@example.com')  # Set your default value
    phone_number = models.CharField(max_length=15)
    skills = models.TextField(default='react')
    job_description = models.TextField()

    def __str__(self):
        return f'{self.job_title} - {self.job_position}'


