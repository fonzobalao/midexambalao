from django import forms

class CreateCandidate(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    platform = forms.TextField()

class UpdateCandidate(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    platform = forms.TextField()

class CreatePosition(forms.Form):
    name  = forms.CharField(max_length=20)
    description = forms.TextField(max_length=20)
