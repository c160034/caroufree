from django import forms
from .models import Listing
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        # fields = "__all__"
        exclude = ["slug", "author"]
        labels = {
            "title" : "Title",
            "description" : "Description",
            "image" : "Image",
        }
        error_messages = {
            "title" : {
                "required": "Title must not be empty!",
                "max_length": "PLease enter a shorter title!"
            }
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2' ]
    email = forms.EmailField(required=True)

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

class MessageForm(forms.Form):
    message = forms.CharField(label='', max_length=100)
    image = forms.FileField(required=False)