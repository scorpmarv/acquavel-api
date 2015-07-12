from django.contrib import admin
from .models import Dia, Clase, DiaHorario


admin.site.register([Dia, Clase, DiaHorario])