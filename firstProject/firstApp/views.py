from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def greet(request):
    return HttpResponse("Hello world")

class Hello(View):
    def get(self, request):
        return HttpResponse("Hello to all")