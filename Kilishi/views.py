from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from . models import products, Cart
from django.http import JsonResponse


# Create your views here.
def order(request):
    from . forms import Kili_order
    form = Kili_order()
    if request.method == 'POST':
        form = Kili_order(request.POST) 
        if form.is_valid():
            print("✅ Form is valid! Saving data...")  # Debugging
            form.save()
            return render(request, 'successful.html') 
        else:
            print("❌ Form errors:", form.errors)  # Debugging
    return render(request, 'order.html', {'order':form})

def homepage(request):
    from .models import products
    web_product = products.objects.all()
    web_product_dict = {'prod': web_product}
    return render(request, 'home.html', web_product_dict)

def reserve(request):
    from . forms import Res_order
    form = Res_order()
    if request.method == 'POST':
        form = Res_order(request.POST) 
        if form.is_valid():
            print("✅ Form is valid! Saving data...")  # Debugging
            form.save()
            return render(request, 'res_suc.html') 
        else:
            print("❌ Form errors:", form.errors)  # Debugging
    return render(request, 'res.html', {'res':form})

def menu(request):
    from .models import products
    web_product = products.objects.all()
    web_product_dict = {'prod': web_product}
    return render(request, 'menu.html', web_product_dict)


def add_to_cart(request, products_id):
    product = get_object_or_404(products, id=products_id)

    # Session-based cart
    cart = request.session.get('cart', {})

    if str(products_id) in cart:
        cart[str(products_id)] += 1  # Increase quantity
    else:
        cart[str(products_id)] = 1  # Add new item

    request.session['cart'] = cart  # Save cart to session

    return redirect('menu') 
