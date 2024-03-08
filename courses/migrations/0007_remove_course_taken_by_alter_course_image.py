# Generated by Django 5.0.1 on 2024-03-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='taken_by',
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/media/uploads/'),
        ),
    ]
