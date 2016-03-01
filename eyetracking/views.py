from django.http import HttpResponse

def index(request):
    return HttpResponse("INDEX PAGE")

def about(request):
    return HttpResponse("ABOUT PAGE")

def register(request):
    return HttpResponse("REGISTRATION PAGE")

def login(request):
    return HttpResponse("LOGIN PAGE")

def user(request): #temporary -- <user_name>
    return HttpResponse("USER PAGE")
