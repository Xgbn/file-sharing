from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    peername = forms.CharField(max_length=20)

class NameForm(forms.Form):
    fname = forms.CharField(label = 'fname', max_length = 20)

