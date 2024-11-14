from django.urls import path
from .views import recommend_subject

urlpatterns = [
    path('recommend', recommend_subject, name='recommend_subject'),
]