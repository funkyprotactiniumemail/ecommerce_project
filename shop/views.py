from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ProductForm

# Create your views here.
def shop_home(request):
    return render(request, 'shop/home.html')

@login_required #verified this is correct notation with ChatGPT
def sell_product_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user 
            product.save()
            form.save_m2m()  # ChatGPT
            return redirect('products:product_list')  
    else:
        form = ProductForm()

    return render(request, 'shop/sell_product.html', {'form': form})


