from rest_framework import serializers
from .models import chat_tb

class questionSerializer(serializers.Serializer):
    studentNumber = serializers.IntegerField()
    chattingQuestion = serializers.CharField(max_length=10000)

class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chat_tb
        fields = '__all__'