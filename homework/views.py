from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("Test 2  page")