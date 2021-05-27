from rest_framework import serializers
from .models import task_data

class task_data_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = task_data
        fields = '__all__'