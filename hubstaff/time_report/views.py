import datetime
from django import urls
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.http import urlencode
from requests import HTTPError

from .client import HubstaffApiClient
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
                "auth_token": user["auth_token"],
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
        form = TimeReportForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                data = HubstaffApiClient(
                    form_data["app_token"], form_data["auth_token"]
                ).list_user_projects(form_data["id"])
            except HTTPError as e:
                form.add_error(
                    None, "The Hubstaff responded with an error: {} {}".format(
                        e.response.status_code, e.response.reason)
                )
    else:
        form = TimeReportForm(request.GET)
        if not (form.data.get("app_token") and form.data.get("auth_token") and form.data.get("name") and
                form.data.get("id") and form.data.get("for_date")):
            return HttpResponseRedirect(urls.reverse('index'))

    context = {"form": form}
    return render(request, 'time_report.html', context)
