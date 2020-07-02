from django.shortcuts import render
from .forms import CredentialsForm

def index(request):
    """
    The main view used as an input point to the application, it will as the user for
    credentials (App token, User, Password) to obtain the Auth token for further prcessing
    """
    auth_form = CredentialsForm(request.POST or {})
    context = {"form": auth_form}
    return render(request, 'index.html', context)

def time_report(request):
    """
    The main view for the Time Report. Using the Auth Token retrieves the neccessary data
    and displays to the user as a table. Data can be downloaded to a CSV file.
    """
    return render(request, 'time_report.html')
