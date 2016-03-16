from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from eyetracking.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import gettingdata
from forms import DataGather
from eyetracking.models import GatheredData

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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Eyetracking Account is disabled")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'eyetracking/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def user(request): #temporary -- <user_name>
    data_list = GatheredData.objects.filter(user = request.user)
    context_dict = {'data': data_list}
    return render(request, 'eyetracking/user.html', context_dict)

@login_required
def gather(request):
    if request.POST:
        form = DataGather(request.POST)
        if(form.is_valid()):
            user = request.user
            location = str(form.cleaned_data['location'])
            speed = str(form.cleaned_data['speed'])
            gaze = str(form.cleaned_data['gaze'])
            incident = str(form.cleaned_data['incident'])
            gettingdata.addData(location, speed, gaze, incident, user)
            return HttpResponseRedirect('/')
    else:
        return render(request, 'eyetracking/test.html', {})

@login_required
def edit_user(request):
    user = request.user
    form = UserForm(request.POST or None, initial={'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})
    if request.method == 'POST':
        if (form.is_valid()):
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return HttpResponseRedirect('/user/')
    context = {
        "form": form
    }
    return render(request, 'eyetracking/edituser.html', context)
