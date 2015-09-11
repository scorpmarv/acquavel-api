from django.contrib import admin
from .models import Clase, DiaHorario


admin.site.register([Clase, DiaHorario])