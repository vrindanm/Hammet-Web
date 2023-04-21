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
 
# SIZE_CHOICES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#         ('XL', 'Extra Large'),
#     )

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField(default=0.0)
    # discounted_price=models.FloatField()
    discounted_price = models.FloatField(default=0.0)
    description=models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    sizes = models.CharField(max_length=50, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='S')


    # sizes = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.title

    # composition=models.TextField(default='')
    # prodapp= models.TextField(default='')

    # size = models.CharField(choices=SIZE_CHOICES, max_length=3, blank=True, null=True)

    # sizes = models.ManyToManyField('Size', related_name='product')
    # sizes = models.ManyToManyField('Size', related_name='products')

    
    
# class Size(models.Model):
#     name = models.CharField(max_length=10)
#     def __str__(self):
#         return self.name    




# class Product(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     product_image = models.ImageField(upload_to='product', default='default_product_image.jpg')
#     category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='AP')
  
# class Variation(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     size = models.CharField(max_length=10)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     stock = models.IntegerField()  
    # category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)

     

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
    ordered = models.BooleanField(default=False)
    @property
    def total_cost(self):
        return self.quantity * self.product.selling_price

# SIZE_CHOICES = [
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#         # add more size categories as needed
# ]      
# class SizeChart(models.Model):
#     size = models.CharField(max_length=1, choices=SIZE_CHOICES)
#     measurement = models.CharField(max_length=50) 

