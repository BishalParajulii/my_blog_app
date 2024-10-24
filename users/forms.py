from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel

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


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User 
        fields = ['username' , 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correct call to super()

    # Remove help text for the fields
        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = ProfileModel
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Correct call to super()

    # Remove help text for the fields
        for fieldname in ['image']:
            self.fields[fieldname].help_text = None

