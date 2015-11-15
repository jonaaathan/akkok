# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='staff_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='staff_id',
            field=models.IntegerField(unique=True),
        ),
    ]
