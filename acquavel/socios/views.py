from rest_framework import generics
from .serializers import SocioSerializer
from models import Socio, Ingreso
from django.views.generic.edit import CreateView


class SocioDetail(generics.RetrieveAPIView):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer


class IngresoView(CreateView):
    model = Ingreso
    fields = ['contratacion','fecha']
    success_url = '/admin/'

    def get_context_data(self, **kwargs):
        context = super(IngresoView, self).get_context_data(**kwargs)
        context['opts'] = self.model._meta
        context['add'] = True
        context['original'] = self.object
        context['has_change_permission'] = self.request.user.has_perm("socios.add")
        return context
