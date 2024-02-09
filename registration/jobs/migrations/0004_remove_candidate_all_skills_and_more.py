# Generated by Django 5.0.1 on 2024-02-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_candidate_all_skills_alter_candidate_company_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='all_skills',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='company_email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills',
            field=models.TextField(default='react'),
        ),
    ]
