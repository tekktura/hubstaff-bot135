import datetime
from django import urls
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.http import urlencode

from .forms import CredentialsForm, TimeReportForm
from .apps import Settings

def index(request):
    """
    The main view used as an input point to the application, it will ask the user for
    credentials (App token, User, Password) to obtain the Auth token for further processing
    """
    settings = Settings()
    if request.method == 'POST':
        auth_form = CredentialsForm(request.POST)
        if auth_form.is_valid():
            settings["app_token"] = auth_form.cleaned_data["app_token"]
            settings["username"] = auth_form.cleaned_data["username"]
            settings.save()
            user = auth_form.cleaned_data["user"]
            yesterday = datetime.date.today() - datetime.timedelta(days=1)
            params = {
                "app_token": auth_form.cleaned_data["app_token"],
                "id": user["id"],
                "name": user["name"],
                "for_date": yesterday,
            }
            return HttpResponseRedirect(
                urls.reverse('time_report') + "?" + urlencode(params)
            )
    else:
        auth_form = CredentialsForm(initial=settings)

    context = {"form": auth_form}
    return render(request, 'index.html', context)

def time_report(request):
    """
    The main view for the Time Report. Using the Auth Token retrieves the necessary data
    and displays to the user as a table. Data can be downloaded to a CSV file.
    """
    if request.method == 'POST':
        report_form = TimeReportForm(request.POST)
    else:
        report_form = TimeReportForm(request.GET)

    context = {"form": report_form}
    return render(request, 'time_report.html', context)
