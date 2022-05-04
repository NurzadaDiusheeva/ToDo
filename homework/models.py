from django.db import models
from requests import options

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    person = models.CharField(max_length=100)
    phone_number = models.IntegerField(int)
    date_of_meeting = models.DateTimeField(auto_created=True)
    comment = models.TextField(max_length=1000)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


# В приложении homework создайте модель с именем ToMeet и добавьте эти поля: persone, 
# phone_number, date_of_meeting, comment, is_closed и is_favorite. Выберите правильные типы моделей самостоятельно. 
# Добавьте модель в панель администратора.

