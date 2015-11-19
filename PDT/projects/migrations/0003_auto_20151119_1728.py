# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_curr_phase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iterations_developers',
            name='developer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
