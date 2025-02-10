from django.contrib import admin

from cart.models import Cart

from cart.models import Order_Details,Payment

admin.site.register(Cart)
admin.site.register(Order_Details)
admin.site.register(Payment)
