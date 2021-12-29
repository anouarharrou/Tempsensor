from rest_framework import serializers
from .models import mydb

class mydbserializer(serializers.ModelSerializer):
    class Meta :
        model = mydb
        fields = '__all__'