from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Plan, Socio, Contratacion, Ingreso


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register([Plan, Socio])


class ContratacionAdmin(admin.ModelAdmin):
    raw_id_fields = ("socio",)

class IngresoAdmin(admin.ModelAdmin):
    raw_id_fields = ("contratacion",)


admin.site.register(Contratacion, ContratacionAdmin)
admin.site.register(Ingreso, IngresoAdmin)