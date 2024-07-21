from django.urls import path
from .views import login_view, register_view, account_view, log_out

urlpatterns = [
    path('login/', login_view, name='login'),
    path('log_out/', log_out, name='log_out'),
    path('register/', register_view, name='register'),
    path('acoount/<int:pk>/', account_view, name='account'),
]