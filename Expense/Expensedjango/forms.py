from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction, Target

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title','amount','transaction_type','date','category']

class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['name', 'target_amount','deadline']