from django.urls import path
from .views import IndexView, ContactView, CartView, ChackOutView, ErrorView, ShopView, TestimonialView, shop_detail_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cart/', CartView.as_view(), name='cart'),
    path('404/', ErrorView.as_view(), name='404'),
    path('chackout/', ChackOutView.as_view(), name='chackout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('shop_detail/<slug:name>/', shop_detail_view, name='shop_detail'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
]