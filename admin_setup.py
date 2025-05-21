from django.contrib import admin
from .models import MenuItem, InventoryItem, Table, Reservation, Order

admin.site.register(MenuItem)
admin.site.register(InventoryItem)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
