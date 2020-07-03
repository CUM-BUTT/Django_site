from django import forms

class SomeForm(forms.Form):
     name = forms.CharField(label='name', max_length=30)
     description = forms.CharField(label='description', max_length=1000)
     release_date=forms.DateField(label='release_date')
     rating = forms.IntegerField(label='rating')