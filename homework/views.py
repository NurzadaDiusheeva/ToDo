from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("Это мой первый проект Django - Admin")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("Test 2  page")