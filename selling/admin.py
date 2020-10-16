from django.contrib import admin
from .models import Selling

# Register your models here.


class SellingAdmin(admin.ModelAdmin):
    list_display = ('name_of_phone', 'name_of_customer', 'status','date_time')
    readonly_fields = ('date_time',)
    search_fields = ('status','name_of_customer')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Selling, SellingAdmin)

