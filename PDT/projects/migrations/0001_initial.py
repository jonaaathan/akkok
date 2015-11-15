# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('iteration_number', models.IntegerField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Iterations_Developers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('active', models.BooleanField(default=False)),
                ('developer', models.ForeignKey(to='users.Developer')),
                ('iteration', models.ForeignKey(to='projects.Iteration')),
            ],
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('phrase_type', models.IntegerField(choices=[(1, 'Inception'), (2, 'Elaboration'), (3, 'Construction'), (4, 'Transition')])),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('manager', models.ForeignKey(to='users.Manager')),
            ],
        ),
        migrations.AddField(
            model_name='phrase',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
        migrations.AddField(
            model_name='iteration',
            name='phrase',
            field=models.ForeignKey(to='projects.Phrase'),
        ),
    ]
