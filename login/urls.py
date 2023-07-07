from django.urls import path
from .views import LoginCreateView,PhoneView

urlpatterns = [
    path('login/', LoginCreateView.as_view(), name='login'),
    path('login/error/', PhoneView.as_view(), name='error'),
]
