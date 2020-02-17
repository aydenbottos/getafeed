from django.contrib import admin

from foodtaskerapp.models import Restaurant, Customer, Driver, Meal, Order, OrderDetails

class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', )
    list_filter = ('restaurant', )

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal, MealAdmin)
admin.site.register(Order)
admin.site.register(OrderDetails)
