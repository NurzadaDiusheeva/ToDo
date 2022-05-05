from django.db import models
from requests import options

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    person = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0)
    date_of_meeting = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=1000)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Habits(models.Model):
    name = models.CharField(max_length=100)
    done_for_today = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    comment = models.TextField(max_length=250)

# Задание № 2
# Создайте новую модель с именем  Habits с  полем name, done_for today, important и comment. 
# Создайте новую форму для Habits  и отобразите их в новом Html - файле habits.html.


