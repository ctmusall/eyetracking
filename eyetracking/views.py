from django.http import HttpResponse
from django.shortcuts import render
from eyetracking.forms import UserForm, UserProfileForm

def index(request):
    context_dict = {'boldmessage': "Please select an option below: "}
    return render(request, 'eyetracking/index.html', context_dict)

def about(request):
    return render(request, 'eyetracking/about.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

                profile.save()

            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
        'eyetracking/register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def login(request):
    return HttpResponse("LOGIN PAGE")

def user(request): #temporary -- <user_name>
    return HttpResponse("USER PAGE")
