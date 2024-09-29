from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correct call to super()

        # Remove help text for the fields
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



