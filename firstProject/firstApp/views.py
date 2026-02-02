from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import RentCarForm

def greet(request):
    return HttpResponse("Hello world")

class Hello(View):
    def get(self, request):
        return HttpResponse("Hello to all")
    
# def home(request):
#     form = ReservationForm()

#     if request.method == "POST":
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Success")
#     return render(request, 'index.html', {'form':form})

def home(request):
    form = RentCarForm()
    if request.method == "POST":
        form = RentCarForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Sending one to your location.")
    return render(request, 'index.html', {'form':form})