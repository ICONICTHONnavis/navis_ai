from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import chatSerializer, questionSerializer
from .gpt.answer import chat_answer, get_history_tuple
from user.models import user_tb

# Create your views here.

@api_view(['POST'])
def create_chat(request):
    serializer = questionSerializer(data=request.data)
    if serializer.is_valid():
        studentNumber = serializer.data['studentNumber']
        chattingQuestion = serializer.data['chattingQuestion']
        try:
            user = user_tb.objects.get(student_number=studentNumber)
            chattingAnswer = chat_answer(chattingQuestion, user.id)
            data = {
                "answer": chattingAnswer,
                "question": chattingQuestion,
                "user": user.id
            }
            chat_serializer = chatSerializer(data=data)
            chat_serializer.is_valid(raise_exception=True)
            chat_serializer.save()
            return Response({
                "responseDto": {
                    "chattingAnswer": chattingAnswer,
                },
                "error": None,
                "success": True
            }, status=status.HTTP_200_OK)
        except user_tb.DoesNotExist:
            return Response({
                "error": 4043,
                "success": False
            }, status=status.HTTP_404_NOT_FOUND)
