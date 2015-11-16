# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0003_phase_curr_iteration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('active', models.BooleanField(default=False)),
                ('developer', models.ForeignKey(to='users.Developer')),
                ('iteration', models.ForeignKey(to='projects.Iteration')),
            ],
        ),
        migrations.RemoveField(
            model_name='iterations_developers',
            name='developer',
        ),
        migrations.RemoveField(
            model_name='iterations_developers',
            name='iteration',
        ),
        migrations.DeleteModel(
            name='Iterations_Developers',
        ),
    ]
