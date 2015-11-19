# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20151119_1728'),
        ('users', '0002_auto_20151119_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('staff_id', models.IntegerField(unique=True)),
                ('number_project_involved', models.IntegerField()),
                ('role', models.CharField(max_length=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='developer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='user',
        ),
        migrations.DeleteModel(
            name='Developer',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
