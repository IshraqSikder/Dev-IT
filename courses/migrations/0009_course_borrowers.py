# Generated by Django 5.0.1 on 2024-03-09 19:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_course_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='borrowers',
            field=models.ManyToManyField(blank=True, related_name='borrowed_course', to=settings.AUTH_USER_MODEL),
        ),
    ]