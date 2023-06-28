from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATE_CHOICES=[
    ('AN','Andaman and Nicobar Islands'),
    ('AP','Andhra Pradesh'),
    ('AR','Arunachal Pradesh'),
    ('AS','Assam'),
    ('BR','Bihar'),
    ('CG','Chhattisgarh'),
    ('DN', 'Dadra and Nagar HavelI'),	
    ('DD','Daman and Diu'),	
    ('DL','Delhi'),
    ('GA','Goa'),
    ('GJ','Gujarat'),
    ('HR','Haryana'),
    ('HP','Himachal Pradesh'),
    ('JK','Jharkhand'),
    ('KA','Karnataka'),
    ('KL','Kerala'),
    ('LD','Lakshadweep'),
    ('PY','Pondicherry'),
    ('MP','Madhya Pradesh'),
    ('MH','Maharashtra'),
    ('MN','Manipur'),
    ('ML','Meghalaya'),
    ('MZ','Mizoram'),
    ('NL','Nagaland'),
    ('OR','Odisha'),
    ('PB','Punjab'),
    ('RJ','Rajasthan'),
    ('SK','Sikkim'),
    ('TN','Tamil Nadu'),
    ('TR','Tripura'),
    ('UK','Uttarakhand'),
    ('UP','Uttar Pradesh'),
    ('WB','West Bengal'),
]

CATEGORY_CHOICES=[
    ('AP','All Products'),
    ('NA','New Arrivals'),
    ('TS','T Shirts'),
    ('HS','Hoodies'),
    ('SS','Sweet Shirts'),
]

STATUS_CHOICES= [
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),   
]
SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL','Extra Large'),
]


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    stock = models.IntegerField(default=0)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    # size = models.CharField(choices=SIZE_CHOICES, max_length=1, default='S')
    def __str__(self):
        return self.title

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sizes')
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size

# class Size(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sizes')
#     size = models.CharField(max_length=10)
#     stock = models.IntegerField(default=0)

#     def __str__(self):
#         return self.size



class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
     
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
         return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # size = models.CharField(max_length=10, default='S')
    size = models.CharField(max_length=10, default='N/A')
    ordered = models.BooleanField(default=False)
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=100,blank=True,null=True)
    paid=models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    # size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)  
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price


class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=None) 






