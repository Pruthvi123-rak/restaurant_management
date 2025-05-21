from django.shortcuts import render
from .models import MenuItem, Order, Reservation, InventoryItem

def dashboard(request):
    orders = Order.objects.all()
    reservations = Reservation.objects.all()
    menu = MenuItem.objects.all()
    inventory = InventoryItem.objects.all()
    return render(request, 'core/dashboard.html', {
        'orders': orders,
        'reservations': reservations,
        'menu': menu,
        'inventory': inventory,
    })
