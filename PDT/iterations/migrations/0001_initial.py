# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('running', models.CharField(max_length=1, choices=[('P', 'Paused'), ('R', 'Running'), ('E', 'END')], default='P')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('total_duration', models.DurationField(default=datetime.timedelta(0))),
            ],
        ),
    ]
