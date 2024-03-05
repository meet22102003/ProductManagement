from django.contrib import admin
from .models import producttable,registertable,carttable

# Register your models here.

class showproducts(admin.ModelAdmin):
    list_display = ["name","price","description","product_photo"]
    list_per_page = 2
    list_filter = ["price"]
    list_editable = ["price"]
    search_fields = ["name","showproducts"]
admin.site.register(producttable,showproducts)

class showregister(admin.ModelAdmin):
    list_display = ["name","email","role"]
admin.site.register(registertable,showregister)

class showcart(admin.ModelAdmin):
    list_display = ["userid","productid","quantity","totalamount","cartstatus","orderid"]
admin.site.register(carttable,showcart)