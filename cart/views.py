from django.shortcuts import redirect, render
from products.models import Product

def cart_view(request):
    cart = request.session.get('cart', {})  # Get cart from session (or empty dict)
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        item_total = product.price * quantity
        total += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    context = {
        'cart_items': cart_items,
        'total': total
    }

    return render(request, 'cart/cart.html', context)

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1 
    request.session['cart'] = cart  
    return redirect('cart:cart_view')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)  
    request.session['cart'] = cart
    return redirect('cart:cart_view')

def update_quantity(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart[str(product_id)] = quantity
        else:
            cart.pop(str(product_id), None)
        request.session['cart'] = cart
    return redirect('cart:cart_view')



def order_confirmation(request):
    return render(request, 'cart/order_confirmation.html')


def get_cart_items(request):
    cart = request.session.get('cart', {})
    items = []

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        total_price = product.price * quantity

        items.append({
            "product": product,
            "quantity": quantity,
            "total_price": total_price,
        })

    return items


def checkout_view(request):
    items = get_cart_items(request)
    total = sum(item["total_price"] for item in items)

    return render(request, "cart/checkout.html", {
        "items": items,
        "total": total,
    })

# import os
# print(os.path.exists(os.path.join('cart', 'templates', 'cart', 'checkout.html'))) # uncomment if you want to test debugging

def checkout_confirm(request):
    
    return render(request, 'cart/checkout_confirm.html')