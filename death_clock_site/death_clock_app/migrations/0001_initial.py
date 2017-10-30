# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1024)),
                ('impact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cause_Of_Death',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=4096)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='impact_type',
            field=models.ForeignKey(to='death_clock_app.Cause_Of_Death'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='death_clock_app.Question'),
        ),
    ]
