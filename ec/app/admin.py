from django.contrib import admin
from . models import Customer,Product,Cart,Contact,Wishlist
# ,Variation
# from .forms import VariationForm

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','category','product_image']

@admin.register(Customer)  
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','address','locality','city','state','zipcode'] 

# admin.site.register(Contact)

@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['name','email','message']

# class VariationInline(admin.TabularInline):
#     model = Variation
#     form = VariationForm

# class ProductAdmin(admin.ModelAdmin):
#     inlines = [VariationInline]

# admin.site.register(Product, ProductAdmin)

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']
