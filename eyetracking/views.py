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
from django.db.models import Avg, Max

def index(request):
    return render(request, 'eyetracking/index.html')

def about(request):
    return render(request, 'eyetracking/about.html')

@login_required
def user(request): #temporary -- <user_name>
    data_list = GatheredData.objects.filter(user = request.user)
    data_count_jan = GatheredData.objects.filter(user = request.user, created_date__month = 1).count()
    data_count_feb = GatheredData.objects.filter(user = request.user, created_date__month = 2).count()
    data_count_mar = GatheredData.objects.filter(user = request.user, created_date__month = 3).count()
    data_count_apr = GatheredData.objects.filter(user = request.user, created_date__month = 4).count()
    data_count_may = GatheredData.objects.filter(user = request.user, created_date__month = 5).count()
    data_count_jun = GatheredData.objects.filter(user = request.user, created_date__month = 6).count()
    data_count_jul = GatheredData.objects.filter(user = request.user, created_date__month = 7).count()
    data_count_aug = GatheredData.objects.filter(user = request.user, created_date__month = 8).count()
    data_count_sep = GatheredData.objects.filter(user = request.user, created_date__month = 9).count()
    data_count_oct = GatheredData.objects.filter(user = request.user, created_date__month = 10).count()
    data_count_nov = GatheredData.objects.filter(user = request.user, created_date__month = 11).count()
    data_count_dec = GatheredData.objects.filter(user = request.user, created_date__month = 12).count()

    data_per_month = [[1,data_count_jan], [2, data_count_feb], [3, data_count_mar], [4, data_count_apr],
    [5, data_count_may], [6, data_count_jun], [7, data_count_jul], [8, data_count_aug], [9, data_count_sep],
    [10, data_count_oct], [11, data_count_nov], [12, data_count_dec]]

    avg_data_speed = GatheredData.objects.aggregate(Avg('speed')).values()
    max_speed_user = GatheredData.objects.filter(user = request.user).aggregate(Max('speed')).values()

    print(max_speed_user)

    ds = DataPool(
       series=
        [{'options': {
            'source': GatheredData.objects.filter(user = request.user)},
          'terms': [
            'location',
            'speed']}
         ])

    cht = Chart(
        datasource = ds,
        series_options =
          [{'options':{
              'type': 'column',
              'stacking': False},
            'terms':{
              'location': [
                'speed']
              }}],
        chart_options =
          {'title': {
               'text': 'Speed by Location'},
           'xAxis': {
                'title': {
                   'text': 'Location'}}})
    ds_b = DataPool(
       series=
        [{'options': {
            'source': GatheredData.objects.filter(user = request.user)},
          'terms': [
            'created_date',
            'speed']}
         ])

    cht_b = Chart(
        datasource = ds_b,
        series_options =
          [{'options':{
              'type': 'pie',
              'stacking': False},
            'terms':{
              'created_date': [
                'speed']
              }}],
        chart_options =
          {'title': {
               'text': 'Highest Speed by Date'}},)

    context_dict = {'data': data_list, 'charts': [cht, cht_b], 'test': data_per_month,}
    return render(request, 'eyetracking/user.html', context_dict)

def gather(request):
    if request.POST:
        form = DataGather(request.POST)
        if(form.is_valid()):
            user = request.user
            location = str(form.cleaned_data['location'])
            speed = int(form.cleaned_data['speed'])
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
    user = request.user
    ds = DataPool(
       series=
        [{'options': {
            'source': GatheredData.objects.filter()},
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
