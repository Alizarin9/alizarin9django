from django.shortcuts import render
from rest_framework import viewsets

from .models import task_data
from .serializers import task_data_serializer

class task_data_view(viewsets.ModelViewSet):
    queryset = task_data.objects.all()
    serializer_class = task_data_serializer
