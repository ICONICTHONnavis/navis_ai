from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import complete_tb, subject_tb
from .serializers import recommendSerializer
from user.models import user_tb
from .utils import gen_desc

@api_view(['POST'])
def recommend_subject(request):
    serializer = recommendSerializer(data=request.data)
    if serializer.is_valid():
        studentNumber = serializer.data['studentNumber']
        try:
            user = user_tb.objects.get(student_number=studentNumber)
            desc = gen_desc(user.id)
            return Response({
                "responseDto": desc,
                "error": None,
                "success": True
            }, status=status.HTTP_200_OK)
        except user_tb.DoesNotExist:
            return Response({
                "error": 4043,
                "success": False
            }, status=status.HTTP_404_NOT_FOUND)