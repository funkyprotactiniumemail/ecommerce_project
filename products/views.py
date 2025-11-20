from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q

# def product_list_view(request):
#     products = Product.objects.all()
#     return render(request, 'products/product_list.html', {'products': products})

def product_list(request):
    query = request.GET.get('q')  # Get search query from URL ?q=
    print("Search query:", query)
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()
    print("Filtered products:", products)
    context = {
        'products': products,
    }    
    return render(request, 'products/product_list.html', context)

def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product':product})

def create_product_view(request):
    return render(request, 'products/create_product.html')

def edit_product_view(request, product_id):
    return render(request, 'products/edit_product.html')

def search_view(request):
    return render(request, 'products/search.html')

