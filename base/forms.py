from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['description', 'location', 'user']

    description = forms.CharField(
       label='Description',
       max_length=50,
       widget=forms.TextInput(attrs={
          'class': 'border p-2 rounded-md m-4'
       })
    )   
    location = forms.CharField(
       label='location',
       widget=forms.TextInput(attrs={
          'class':'border p-2 rounded-md m-4'
       })
    ) 

class CustomForm(UserCreationForm):
  class Meta:
    model = User
    fields = UserCreationForm.Meta.fields

  username = forms.CharField(widget = forms.TextInput(attrs={
        'placeholder': 'eg Jay',
        'class': 'w-25  my-3 rounded-md border-0 py-2 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 md:placeholder-gray-900 md:focus:placeholder-red-600 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
    }) ,label='Username')
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password as *****',
        'class': 'w-25  my-3 rounded-md border-0 py-2 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 md:placeholder-gray-900 md:focus:placeholder-red-600 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
    }), label='Password')
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password again as *****',
        'class': 'w-25  my-3 rounded-md border-0 py-2 pl-7 pr-20 text-gray-900 ring-1 ring-inset ring-gray-300 md:placeholder-gray-900 md:focus:placeholder-red-600 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6'
    }), label='Password again!')

