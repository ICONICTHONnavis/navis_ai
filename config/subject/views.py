from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import complete_tb, subject_tb
from .serializers import recommendSerializer
from user.models import user_tb
from chat.serializers import chatSerializer
from .utils import gen_desc, subject_recommend, multi_recommend

@api_view(['POST'])
def recommend_subject(request):
    serializer = recommendSerializer(data=request.data)
    if serializer.is_valid():
        studentNumber = serializer.data['studentNumber']
        try:
            user = user_tb.objects.get(student_number=studentNumber)
            # desc = gen_desc(user.id)
            # rec = subject_recommend(user.nl_description)
            rec = multi_recommend(user.nl_description)
            data = {
                "answer": rec,
                "question": "나의 학점 정보를 기반으로 들을만한 전공 수업 추천해줘",
                "user": user.id
            }
            chat_serializer = chatSerializer(data=data)
            chat_serializer.is_valid(raise_exception=True)
            chat_serializer.save()
            return Response({
                "responseDto": {
                    "chattingQuestion": "나의 학점 정보를 기반으로 들을만한 전공 수업 추천해줘",
                    "chattingAnswer": rec,
                },
                "error": None,
                "success": True
            }, status=status.HTTP_200_OK)
        except user_tb.DoesNotExist:
            return Response({
                "error": 4043,
                "success": False
            }, status=status.HTTP_404_NOT_FOUND)