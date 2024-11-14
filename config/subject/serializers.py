from rest_framework import serializers
from .models import complete_tb

class recommendSerializer(serializers.Serializer):
    studentNumber = serializers.IntegerField()

class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = complete_tb
        fields = '__all__'