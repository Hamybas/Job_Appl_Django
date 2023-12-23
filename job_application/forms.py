from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=80)
    date = forms.DateField()
    status = forms.CharField(max_length=80)
