from django import forms


class contactforemail(forms.Form):
    fromemail=forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Your Email'}))
    subject=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message=forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder': 'Message'}))
 