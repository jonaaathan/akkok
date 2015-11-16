# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_curr_phase'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='curr_iteration',
            field=models.IntegerField(default=0),
        ),
    ]
