# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaHorario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desdehora', models.TimeField()),
                ('hastahora', models.TimeField()),
                ('dia', models.ForeignKey(to='actividades.Dia')),
            ],
        ),
        migrations.RemoveField(
            model_name='diahorarioclase',
            name='clase',
        ),
        migrations.RemoveField(
            model_name='diahorarioclase',
            name='dia',
        ),
        migrations.DeleteModel(
            name='DiaHorarioClase',
        ),
        migrations.AddField(
            model_name='clase',
            name='horarios',
            field=models.ManyToManyField(to='actividades.DiaHorario'),
        ),
    ]
