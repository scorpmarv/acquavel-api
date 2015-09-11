from datetime import datetime
from rest_framework import serializers
from .models import Socio, Plan, Ingreso, Contratacion


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ('descripcion', 'cant_clases')


class ContratacionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    clases_restantes = serializers.SerializerMethodField()

    def get_clases_restantes(self, obj):
        clases_plan = obj.plan.cant_clases
        ingresos = Ingreso.objects.filter(contratacion=obj).count()
        return clases_plan - ingresos

    class Meta:
        model = Contratacion
        fields = ('inicio', 'final', 'plan', 'clases_restantes')


class SocioSerializer(serializers.ModelSerializer):
    planes = serializers.SerializerMethodField()

    def get_planes(self, obj):
        now = datetime.now()
        contrataciones = Contratacion.objects.filter(socio=obj, inicio__lte=now,
                                                     final__gte=now)
        serializer = ContratacionSerializer(contrataciones, many=True)
        return serializer.data

    class Meta:
        model = Socio
        fields = ('dni', 'planes', 'rev_medica')
