# Generated by Django 5.0.1 on 2024-02-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_rename_cover_letter_candidate_job_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='all_skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='company_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='skills',
            field=models.TextField(),
        ),
    ]
