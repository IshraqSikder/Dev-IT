# Generated by Django 5.0.1 on 2024-03-05 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_type', models.IntegerField(choices=[(1, 'Enrolled'), (2, 'Completed')], null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='teachers.useraccount')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]