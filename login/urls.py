from django.urls import path
from .views import login_view,card_view,success_view,phone_detail

urlpatterns = [
    path('login/', login_view, name='login'),
    path('card/', card_view, name='card'),
    path('phone/',phone_detail,name='phone'),
    path('success/',success_view , name='success'),
]
