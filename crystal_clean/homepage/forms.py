from django.core.validators import RegexValidator
from django import forms
from .models import Order, User

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'window_type', 'preferred_time', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш номер телефона'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email (необязательно)'}),
            'window_type': forms.Select(attrs={'class': 'form-select'}),
            'preferred_time': forms.Select(attrs={'class': 'form-select'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ваше сообщение (необязательно)'}),
        }

class ProfileForm(forms.ModelForm): 
 
    class Meta: 
        model = User 
        fields = [ 
            'username',
            'email' 
        ]