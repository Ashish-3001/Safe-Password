from django import forms

class DetailsForm(forms.Form):
    name = forms.CharField(label='Name of the Application')
    username = forms.CharField(label='Username of that Application')
    password = forms.CharField(label='Password of that Application')