from django.urls import path
from .views import Create_ProductView

urlpatterns = [
    path('create_product/', Create_ProductView.as_view(), name="create_product")
]