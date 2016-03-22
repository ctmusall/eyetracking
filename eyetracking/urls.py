from django.conf.urls import patterns, url
from eyetracking import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    url(r'^user/', views.user, name='user'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^gather/', views.gather, name='gather'),
    url(r'^edituser/', views.edit_user, name='edituser'),
    url(r'^chart/', views.speed_chart, name='chart')
]
