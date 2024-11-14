from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import chatSerializer, questionSerializer
from .gpt.answer import chat_answer
from user.models import user_tb
from subject.utils import gen_desc

@api_view(['POST'])
def create_chat(request):
    serializer = questionSerializer(data=request.data)
    if serializer.is_valid():
        studentNumber = serializer.data['studentNumber']
        chattingQuestion = serializer.data['chattingQuestion']
        try:
            user = user_tb.objects.get(student_number=studentNumber)
            if user.nl_description == None:
                user.nl_description = gen_desc(user.id)
                user.save()
            chattingAnswer = chat_answer(chattingQuestion, user.id, user.nl_description)
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
