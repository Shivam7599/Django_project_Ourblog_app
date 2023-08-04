from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms 
from django.contrib.auth.models import User
from Ourblog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('author_name', 'bio', 'profilepic', 'web_url', 'fb_url', 'twitter_url', 'insta_url', 'pinterest_url', 'github_url')
        widgets = {
            'bio' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the title-'}),
            # 'profilepic' : forms.ImageField(attrs={'class': 'form-control', 'placeholder' : 'Author'}),
            'web_url' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the title-'}),
            'fb_url' : forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url' : forms.TextInput(attrs={'class': 'form-control'}),
            'insta_url' : forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url' : forms.TextInput(attrs={'class': 'form-control'}),
            'github_url' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Enter the Text-'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = User
        # fields = "__all__"
        fields = ("first_name", "last_name", "email", "username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class Edit_Profile_Form(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    last_login = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
    is_superuser = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check', 'placeholder': ''}))
    is_staff = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check', 'placeholder': ''}))
    is_active = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check', 'placeholder': ''}))
    date_joined = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))

    class Meta:
        model = User
        # fields = "__all__"
        fields = ("username", "first_name", "last_name", "email", "date_joined", "is_active", "is_staff", "is_superuser", "last_login")




class Password_changing_Form(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        # fields = "__all__"
        fields = ("old_password", "new_password1", "new_password2")