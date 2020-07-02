from django.urls import path

from . import views

urlpatterns = [
    # main URL will be used to obtain credentials from user and get Auth Key
    path('', views.index, name="index"),
    # this view is the time report
    path('time_report', views.time_report, name="time_report"),
]
