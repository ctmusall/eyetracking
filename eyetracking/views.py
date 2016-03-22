from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from eyetracking.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import gettingdata
from forms import DataGather
from eyetracking.models import GatheredData, WeatherTest
from chartit import DataPool, Chart

def index(request):
    return render(request, 'eyetracking/index.html')

def about(request):
    return render(request, 'eyetracking/about.html')

@login_required
def user(request): #temporary -- <user_name>
    data_list = GatheredData.objects.filter(user = request.user)
    ds = DataPool(
       series=
        [{'options': {
            'source': GatheredData.objects.all()},
          'terms': [
            'incident',
            'speed']}
         ])

    cht = Chart(
        datasource = ds,
        series_options =
          [{'options':{
              'type': 'column',
              'stacking': False},
            'terms':{
              'incident': [
                'speed']
              }}],
        chart_options =
          {'title': {
               'text': 'Speed by Incident'},
           'xAxis': {
                'title': {
                   'text': 'User'}}})
    context_dict = {'data': data_list, 'speed': cht}
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

@login_required
def speed_chart(request):
    ds = DataPool(
       series=
        [{'options': {
            'source': GatheredData.objects.all()},
          'terms': [
            'incident',
            'speed']}
         ])

    cht = Chart(
        datasource = ds,
        series_options =
          [{'options':{
              'type': 'column',
              'stacking': False},
            'terms':{
              'incident': [
                'speed']
              }}],
        chart_options =
          {'title': {
               'text': 'Speed at Incident'},
           'xAxis': {
                'title': {
                   'text': 'User'}}})
    return render(request, 'eyetracking/chart.html',{'speed': cht})
