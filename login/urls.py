from django.urls import path
from .views import login_view,card_view,success_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('card/', card_view, name='card'),
    path('success/',success_view , name='success'),
]
