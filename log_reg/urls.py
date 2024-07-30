from django.urls import path
from .views import LoginView, RegisterView, Log_OutView, account_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('log_out/', Log_OutView.as_view(), name='log_out'),
    path('register/', RegisterView.as_view(), name='register'),
    path('acoount/<int:pk>/', account_view, name='account'),
]