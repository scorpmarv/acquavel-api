from rest_framework import generics
from .serializers import ClaseSerializer
from models import Clase


class ClaseList(generics.ListAPIView):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

