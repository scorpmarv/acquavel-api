# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class DiaHorario(models.Model):
    DIA_LUNES = 0
    DIA_MARTES = 1
    DIA_MIERCOLES = 2
    DIA_JUEVES = 3
    DIA_VIERNES = 4
    DIA_SABADO = 5
    DIA_DOMINGO = 6

    DIAS_OPCIONES = (
        (DIA_LUNES, _(u'Lunes')),
        (DIA_MARTES, _(u'Martes')),
        (DIA_MIERCOLES, _(u'Miercoles')),
        (DIA_JUEVES, _(u'Jueves')),
        (DIA_VIERNES, _(u'Viernes')),
        (DIA_SABADO, _(u'Sabado')),
        (DIA_DOMINGO, _(u'Domingo')),
    )
    dia = models.PositiveSmallIntegerField(choices=DIAS_OPCIONES, verbose_name=_(u'Día'))
    desdehora = models.TimeField()
    hastahora = models.TimeField()

    def __unicode__(self):
        return u'{}, {} - {}'.format(self.get_dia_display(), self.desdehora, self.hastahora)

    class Meta:
        unique_together = (("dia", "desdehora", "hastahora"),)
        ordering = ['dia', 'desdehora']


class Clase(models.Model):
    descripcion = models.CharField(max_length=200)
    horarios = models.ManyToManyField(DiaHorario)

    def __unicode__(self):
        return str(self.descripcion)
