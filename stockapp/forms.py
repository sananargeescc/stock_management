from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from stockapp.models import Customer_Registration, Login_view, Stock


class cust_form(forms.ModelForm):

    class Meta:
        model = Customer_Registration
        exclude = ("user",)

class user_reg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,validators=[
        RegexValidator(regex='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,}$',message='please enter valid number')])
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ("username","password1","password2")

class stock_form(forms.ModelForm):

    class Meta:
        model = Stock
        fields = "__all__"
