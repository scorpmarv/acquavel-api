from django.shortcuts import render
from rest_framework import generics
from .serializers import SocioSerializer
from models import Socio


class SocioList(generics.ListCreateAPIView):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer


class SocioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer