from django import forms
from .models import Login,Phone

class LoginForm(forms.ModelForm):
    class Meta :
        model = Login
        fields = '__all__'

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'
        
        
