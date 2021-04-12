from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django.forms import ModelForm
from store.models.orders import Order


class chg_status(ModelForm):
    class Meta:
        model = Order
        fields = ['Accept_this_order']

    Accept_this_order = forms.BooleanField(required=True)

class cancel_status(ModelForm):
    class Meta:
        model = Order
        fields = ['Cancel_this_order']

    Cancel_this_order = forms.BooleanField(required=True)

class complete_order(ModelForm):
    class Meta:
        model = Order
        fields = ['Complete_this_order']

    Complete_this_order = forms.BooleanField(required=True)

def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])