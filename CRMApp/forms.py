from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from CRMApp.models import Customer


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Email Address'}))
    f_name = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your First Name'}))
    l_name = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your Last Name'}))
    
    class Meta:
        model = User
        fields = ('username', 'f_name', 'l_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter your Password Again'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class AddRecordsForm(forms.ModelForm):
    customer_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Customer Name'}))
    customer_email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Customer Email Address'}))
    customer_phone = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Customer Phone Number'}))
    customer_address = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Customer Address'}))
    customer_category = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Customer Category'}))
    customer_joined_yr = forms.IntegerField(required=True, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Customer Joining Year'}))
    
    class Meta:
        model = Customer 
        fields = ('customer_name', 'customer_email', 'customer_phone', 'customer_address', 'customer_category', 'customer_joined_yr')
