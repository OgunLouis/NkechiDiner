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

    # Retrieve existing cart or create an empty one
    cart = request.session.get('cart', {})

    if str(products_id) in cart:
        if isinstance(cart[str(products_id)], int):
            cart[str(products_id)] = {
                'product_name': product.product_name,
                'price': product.price,
                'quantity': cart[str(products_id)] + 1
            }
        else:
            cart[str(products_id)]['quantity'] += 1  
    else:
        cart[str(products_id)] = {
            'product_name': product.product_name,
            'price': product.price,
            'quantity': 1
        }

    # Save updated cart back to session
    request.session['cart'] = cart
    request.session.modified = True 

    print("🛒 Cart Updated:", request.session['cart'])  # Debugging output

    return redirect('menu')  

def view_cart(request):
    cart = request.session.get('cart', {}) 
    return render(request, 'cart.html', {'cart': cart})
