from rest_framework import serializers
from Home.models import home


class homeSerializer(serializers.ModelSerializer):
    class Meta:
        model = home
        fields = ('name', 'username', 'password','id')
        
