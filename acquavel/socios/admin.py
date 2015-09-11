from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.conf.urls import include, url

from .models import Plan, Socio, Contratacion, Ingreso
from .views import IngresoView


# admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register([Plan, Socio])


class ContratacionAdmin(admin.ModelAdmin):
    raw_id_fields = ("socio",)


class IngresoAdmin(admin.ModelAdmin):
    raw_id_fields = ("contratacion",)

    def get_urls(self):
        urls = super(IngresoAdmin, self).get_urls()
        my_urls = [
            url(r'^add/$', self.admin_site.admin_view(IngresoView.as_view()), name='socios_ingreso_add'),
        ]
        return my_urls + urls


admin.site.register(Contratacion, ContratacionAdmin)
admin.site.register(Ingreso, IngresoAdmin)


