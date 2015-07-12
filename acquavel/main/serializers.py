from rest_framework import serializers
from .models import Socio, Plan, Ingreso, Contratacion


class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = ('contratacion', 'fecha')


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ('descripcion', 'cant_clases')


class ContratacionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)

    class Meta:
        model = Contratacion
        fields = ('inicio', 'final', 'plan')


class SocioSerializer(serializers.ModelSerializer):
    planes = ContratacionSerializer(source='contratacion_set', many=True)

    class Meta:
        model = Socio
        fields = ('dni', 'planes')
        # fields = ('dni', 'planes')
