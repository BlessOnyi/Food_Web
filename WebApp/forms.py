from django import forms

class search_details(forms.Form):
    query = forms.CharField(label='search food or vendor',max_length=250)