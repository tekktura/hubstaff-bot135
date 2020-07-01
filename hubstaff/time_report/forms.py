from django import forms

class CredentialsForm(forms.Form):
    """
    This form is used to obtain user credentials as well as the App Token. The password is not
    saved anywhere and is only used once. App Token and user name mae be saved to a local file.
    """
    app_token = forms.CharField(
        label="Hubstaff App Token",
        required=True,
        help_text="Please find your app token in <a href=''><a>"
    )
    username = forms.EmailField(
        label="Hubstaff Username",
        required=True,
        help_text="Please provide your Hubstaff username (as email)"
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Hubstaff Password",
        required=True,
       help_text="IMPORTANT: Your password will not be stored anywhere"
    )