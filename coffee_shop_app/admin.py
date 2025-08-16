from django.contrib import admin
from coffee_shop_app .models import Inventory,Sales_Data,Contact,Bookings
# Register your models here.
admin.site.register(Inventory)
admin.site.register(Sales_Data)
admin.site.register(Contact)
admin.site.register(Bookings)
