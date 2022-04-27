from django.http import HttpResponse
from django.shortcuts import render
from .models import ToDo

def homework(request):
    return render(request, "index.html")

def todo_list(request):
    return render(request, "homework.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("Test 2  page")
