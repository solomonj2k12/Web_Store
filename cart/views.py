from django.shortcuts import render, reverse, redirect

# Create your views here.

def view_cart(request):
    """
    this view displays everything in the cart
    """
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """
    add a qaunity to item in cart
    """
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('store'))
    
    
def adjust_cart(request, id):
    """
    adjust quantity in the cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
    
    