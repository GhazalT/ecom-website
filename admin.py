from django.contrib import admin
from .models import Product,Order
admin.site.site_header="E-commerce Site"
admin.site.site_title="hazel shopping"
admin.site.index_title="manage hazel shopping"




class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    list_display = ("title","price","discount_price","category","image","description")
    search_fields =("title",)
    actions =("change_category_to_default",)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
