from django import forms
from django.core.exceptions import ValidationError
from requests import HTTPError

from .client import HubstaffApiClient


class CredentialsForm(forms.Form):
    """
    This form is used to obtain user credentials as well as the App Token. The password is not
    saved anywhere and is only used once. App Token and username may be saved to a local file.
    """
    app_token = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 45, 'rows': 3}),
        label="App Token",
        required=True,
        help_text="Please find your app token in https://app.hubstaff.com/developer/my_apps"
    )
    username = forms.EmailField(
        label="Username",
        required=True,
        help_text="Please provide your Hubstaff username (email)"
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
        required=True,
        help_text="IMPORTANT: Your password will not be stored anywhere"
    )

    def clean(self):
        try:
            user_data = HubstaffApiClient(self.cleaned_data["app_token"]).authenticate(
                self.cleaned_data["username"],
                self.cleaned_data["password"],
            )
        except HTTPError as e:
            if e.response.status_code == 401:
                raise ValidationError("Invalid email and/or password")
            elif e.response.status_code == 403:
                raise ValidationError("API access is only for organizations on an active plan")
            else:
                raise(ValidationError("Authentication failed ({} {})".format(
                    e.response.status_code, e.response.reason
                )))
        self.cleaned_data["user"] = user_data
        return self.cleaned_data


class TimeReportForm(forms.Form):
    """
    This form is used to provide date for which time report will be obtained.
    """
    FORMAT_CHOICES = (
        ("html", "HTML"),
        ("txt", "Plain Text"),
        ("csv", "Excel/CSV"),
    )

    for_date = forms.DateField(
        label="Date",
        required=True,
        help_text="Accepts a variety of date formats"
    )
    app_token = forms.CharField(widget=forms.HiddenInput)
    auth_token = forms.CharField(widget=forms.HiddenInput)
    name = forms.CharField(widget=forms.HiddenInput)
    id = forms.IntegerField(widget=forms.HiddenInput)
    format = forms.ChoiceField(
        widget=forms.RadioSelect,
        label="Output format",
        required=True,
        choices=FORMAT_CHOICES,
        initial="html"
    )