from django.urls import path
from . import views

app_name = 'products'  

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.create_product_view, name='create_product'),
    path('<int:product_id>/edit/', views.edit_product_view, name='edit_product'), # we put here for later
    path('search/', views.search_view, name='search'), # we put here for later
]
