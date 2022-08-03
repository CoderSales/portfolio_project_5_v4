"""
Generates Django's the automatic admin interface.
Reads metadata from your models to provide a quick,
model-centric interface.
Imports admin Order and OrderLineItem models.
Defines OrderLineItemAdminInline and OrderAdmin classes.
https://docs.djangoproject.com/en/3.1/ref/contrib/admin/
https://stackoverflow.com/questions/47752994/purpose-of-admin-py-file-in-app-in-django-project#:~:text=The%20admin.py%20file%20is,also%20customize%20your%20admin%20panel.
"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    OrderLineItemAdminInline class takes admin.TabularInlin
    as an argument and generates
    inlines, fields, list, and ordering
    parameters.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """Includes lists of fields to be calculated
    the model methods"""
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
