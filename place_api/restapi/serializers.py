from place_api.restapi.models import Place 
from rest_framework import serializers 

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place 
        fields = ['id', 'name', 'reason', 'dateAdded']

    