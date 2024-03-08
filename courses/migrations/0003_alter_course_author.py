# Generated by Django 5.0.1 on 2024-03-05 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_borrowers_course_taken_by'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teachers.useraccount'),
        ),
    ]
