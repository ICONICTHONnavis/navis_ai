from django.urls import path
from .views import create_chat

urlpatterns = [
    path('question', create_chat, name='create_chat'),
]