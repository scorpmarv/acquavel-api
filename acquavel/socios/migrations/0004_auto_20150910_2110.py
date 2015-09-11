# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0003_socio_rev_medica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='rev_medica',
            field=models.DateField(null=True, verbose_name='Revisaci\xf3n m\xe9dica', blank=True),
        ),
    ]
