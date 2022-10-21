from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        # fields = "__all__"
        exclude = ["slug"]
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