
from django.contrib import admin
from django.urls import path
from .views import *
from covid.views import *
from heartdisease.views import *
from diabetesdisease.views import *
from stokeapp.views import *
from asthmaapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='home'),
    path('index/', index, name='index'),
    path('howitworks/', howitworks, name='howitworks'),
    path('getstarted/', getstarted, name='getstarted'),
    path('visualization/', visualization, name='visualization'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin_log, name='admin'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    path('CovidInput/', CovidInput, name='CovidInput'),
    path('validate_details/', validate_details, name='validate_details'),
    path('predict_heart/', predict_heart, name='predict_heart'),
    path('heartInput/', heartInput, name='heartInput'),
    path('diabetesInput/', diabetesInput, name='diabetesInput'),
    path('Diabetes_validate/', Diabetes_validate, name = 'Diabetes_validate'),
    path('stokeinput/', stokeinput, name="stokeinput"),
    path('predictStoke/', predictStoke, name = "predictStoke"),
    path('asthmainput/', asthmainput, name="asthmainput"),
    path('predictasthma/', predictasthma, name="predictasthma"),
    
]
