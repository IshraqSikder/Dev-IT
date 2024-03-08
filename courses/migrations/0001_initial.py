# Generated by Django 5.0.1 on 2024-03-05 15:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Courses/media/uploads/')),
                ('borrowers', models.ManyToManyField(blank=True, related_name='enrolled_course', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='categories.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.course')),
            ],
        ),
    ]