# Generated by Django 5.0.2 on 2024-02-29 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniconnectapp', '0006_campus_is_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusRegistrationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('campus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uniconnectapp.campus')),
            ],
        ),
    ]