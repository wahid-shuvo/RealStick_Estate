from rest_framework import serializers
from .models import Relator


class RelatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relator
        fields = '__all__'
