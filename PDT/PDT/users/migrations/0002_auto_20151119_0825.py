# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='name',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='password',
        ),
        migrations.AddField(
            model_name='developer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='manager',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
