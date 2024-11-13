from django.db import models
from user.models import user_tb

class chat_tb(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    question = models.TextField()
    user = models.ForeignKey(user_tb, on_delete=models.CASCADE)

    class Meta:
        db_table = 'chat_tb'

# Create your models here.
