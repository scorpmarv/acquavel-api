# -*- coding: utf-8 -*-
from django.db import models


class Plan(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    cant_clases = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = u'Planes'

    def __unicode__(self):
        return self.descripcion


class Socio(models.Model):
    dni = models.PositiveIntegerField(primary_key=True)
    planes = models.ManyToManyField(Plan, through='Contratacion')
    rev_medica = models.DateField(blank=True, null=True, verbose_name=u'Revisación médica')

    def __unicode__(self):
        return str(self.dni)


class Contratacion(models.Model):
    plan = models.ForeignKey(Plan)
    socio = models.ForeignKey(Socio)
    inicio = models.DateField()
    final = models.DateField()

    class Meta:
        verbose_name_plural = u'Contrataciones'

    def __unicode__(self):
        return u'{} - {} - {} - {}'.format(self.socio, self.plan, self.inicio, self.final)


class Ingreso(models.Model):
    contratacion = models.ForeignKey(Contratacion)
    fecha = models.DateField()

    def __unicode__(self):
        return u'{} - {}'.format(self.contratacion, self.fecha)
