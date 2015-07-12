from django.db import models


class Dia(models.Model):
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.descripcion)


class DiaHorario(models.Model):
    dia = models.ForeignKey(Dia)
    desdehora = models.TimeField()
    hastahora = models.TimeField()

    def __unicode__(self):
        return '{}, {} - {}'.format(self.dia, self.desdehora, self.hastahora)


class Clase(models.Model):
    descripcion = models.CharField(max_length=200)
    horarios = models.ManyToManyField(DiaHorario)

    def __unicode__(self):
        return str(self.descripcion)
