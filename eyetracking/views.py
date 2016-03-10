from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Please select an option below: "}
    return render(request, 'eyetracking/index.html', context_dict)

def about(request):
    return render(request, 'eyetracking/about.html')

def register(request):
    return HttpResponse("REGISTRATION PAGE")

def login(request):
    return HttpResponse("LOGIN PAGE")

def user(request): #temporary -- <user_name>
    return HttpResponse("USER PAGE")
