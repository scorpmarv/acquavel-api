from rest_framework import serializers
from .models import DiaHorario, Clase


class DiaHorarioSerializer(serializers.ModelSerializer):
    dia = serializers.ReadOnlyField(source='get_dia_display')

    class Meta:
        model = DiaHorario
        fields = ('dia', 'desdehora', 'hastahora',)


class ClaseSerializer(serializers.ModelSerializer):
    horarios = DiaHorarioSerializer(many=True)

    class Meta:
        model = Clase
        fields = ('descripcion', 'horarios',)
