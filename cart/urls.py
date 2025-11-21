from django.urls import path
from . import views

app_name = 'cart'  

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:product_id>/', views.update_quantity, name='update_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    path('checkout/confirm/', views.checkout_confirm, name = 'checkout_confirm')
]
