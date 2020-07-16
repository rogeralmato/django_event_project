from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from website.models import Profile

class SignUpForm(UserCreationForm):
    """
    Signup form. It uses the UserCreation Form.

    Args:
        UserCreationForm 
    """
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

class SignUpProfileForm(forms.ModelForm):
    """
    SignUpProfileForm. It creates a new user Profile. 

    Args:
        ModelForm
    """
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')
    
    def __init__(self, *args, **kwargs):
        super(SignUpProfileForm, self).__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['profile_pic'].widget.attrs['class'] = 'form-control'

class EditUserForm(UserChangeForm):
    """
    EditUserForm. It edits a current user

    Args:
        UserChangeForm 
    """
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
    
class EditProfileForm(forms.ModelForm):
    """
    EditProfileForm. It edits a current profile.

    Args:
        ModelForm
    """

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['bio'].widget.attrs['class'] = 'form-control'


class PasswordChangingForm(PasswordChangeForm):
    """
    PasswordChangingForm. It updates the user password.

    Args:
        PasswordChangeForm 
    """
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
