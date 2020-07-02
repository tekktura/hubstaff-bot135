from django import forms

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