from django.http import HttpResponse
from django.shortcuts import render

def homework(request):
    return HttpResponse("Добро пожаловать в приложение ToDo - Admin)")

def test(request):
    return HttpResponse("Test page")
