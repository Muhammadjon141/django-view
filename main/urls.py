from django.urls import path
from .views import index_view, contact_view, cart_view, chackout_view, error_view, shop_detail_view, shop_view, testimonial_view

urlpatterns = [
    path('', index_view, name='index'),
    path('cart/', cart_view, name='cart'),
    path('404/', error_view, name='404'),
    path('chackout/', chackout_view, name='chackout'),
    path('contact/', contact_view, name='contact'),
    path('shop_detail/<slug:name>/', shop_detail_view, name='shop_detail'),
    path('shop/', shop_view, name='shop'),
    path('testimonial/', testimonial_view, name='testimonial'),
]