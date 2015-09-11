# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_auto_20150712_2019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diahorario',
            options={'ordering': ['dia', 'desdehora']},
        ),
        migrations.AlterField(
            model_name='diahorario',
            name='dia',
            field=models.PositiveSmallIntegerField(verbose_name='D\xeda', choices=[(0, 'Lunes'), (1, 'Martes'), (2, 'Miercoles'), (3, 'Jueves'), (4, 'Viernes'), (5, 'Sabado'), (6, 'Domingo')]),
        ),
        migrations.AlterUniqueTogether(
            name='diahorario',
            unique_together=set([('dia', 'desdehora', 'hastahora')]),
        ),
        migrations.DeleteModel(
            name='Dia',
        ),
    ]
