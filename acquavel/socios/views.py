from rest_framework import generics
from .serializers import SocioSerializer
from models import Socio


class SocioDetail(generics.RetrieveAPIView):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer