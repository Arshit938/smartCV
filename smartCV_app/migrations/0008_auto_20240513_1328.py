# Generated by Django 3.2.12 on 2024-05-13 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartCV_app', '0007_auto_20240513_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedpdf',
            name='jd_pdf',
        ),
        migrations.RemoveField(
            model_name='uploadedpdf',
            name='resume_pdf',
        ),
        migrations.AddField(
            model_name='uploadedpdf',
            name='pdf',
            field=models.FileField(default=None, upload_to='static/pf_files/'),
        ),
        migrations.AlterField(
            model_name='logging',
            name='timestamp',
            field=models.TimeField(default=datetime.datetime(2024, 5, 13, 13, 28, 22, 506897)),
        ),
    ]
