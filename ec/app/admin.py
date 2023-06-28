from django.contrib import admin
from . models import Customer,Product,Cart,Contact,Wishlist,Payment,OrderPlaced,Size



class SizeInline(admin.TabularInline):
    model = Size


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','selling_price','category','product_image']
    inlines = [SizeInline]

@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'size']

@admin.register(Customer)  
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','address','locality','city','state','zipcode'] 

@admin.register(Cart)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['name','email','message']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']



@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status','payment']




