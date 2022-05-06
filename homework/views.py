from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet, Habits

def homework(request):
    return render(request, "index.html")

def todo_list(request):
    return render(request, "homework.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def meeting_list(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"tomeet_list": tomeet_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_tomeet(request):
    form = request.POST
    text = form["tomeet_text"]
    comment = form["comment"]
    phone = form["phone_number"]
    tomeet = ToMeet(person=text, comment=comment, phone_number=phone)
    tomeet.save()
    return redirect(meeting_list)

def habits(request):
    habit_list = Habits.objects.all()
    return render(request, "habits.html", {"habit_list":habit_list})

def add_habit(request):
    form = request.POST
    text = form["habit_text"]
    habit = Habits(name=text)
    habit.save()
    return redirect(habits)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def delete_to_meet(request, id):
    todo = ToMeet.objects.get(id=id)
    todo.delete()
    return redirect(meeting_list)

def mark_to_meet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(meeting_list)

def unmark_to_meet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = False
    tomeet.save()
    return redirect(meeting_list)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)