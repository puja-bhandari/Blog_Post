# Generated by Django 5.0.6 on 2024-06-02 10:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_current_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='current_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
