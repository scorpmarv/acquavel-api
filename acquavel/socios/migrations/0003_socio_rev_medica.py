# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0002_auto_20150804_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='rev_medica',
            field=models.DateField(null=True, verbose_name=b'Revisaci\xc3\xb3n m\xc3\xa9dica', blank=True),
        ),
    ]
