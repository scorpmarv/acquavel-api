# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contratacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicio', models.DateField()),
                ('final', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Contrataciones',
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('contratacion', models.ForeignKey(to='socios.Contratacion')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('cant_clases', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Planes',
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('dni', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('planes', models.ManyToManyField(to='socios.Plan', through='socios.Contratacion')),
            ],
        ),
        migrations.AddField(
            model_name='contratacion',
            name='plan',
            field=models.ForeignKey(to='socios.Plan'),
        ),
        migrations.AddField(
            model_name='contratacion',
            name='socio',
            field=models.ForeignKey(to='socios.Socio'),
        ),
    ]
