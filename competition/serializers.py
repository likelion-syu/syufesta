from .models import Booth
from rest_framework import serializers

class BoothSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booth
        fields ='__all__'