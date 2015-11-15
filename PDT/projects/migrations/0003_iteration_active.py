# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pharse_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteration',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
