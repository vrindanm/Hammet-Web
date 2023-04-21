# from urllib import request
# from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render,redirect
from django.views import View
from . models import Product,Cart, Contact
from .forms import CustomerProfileForm,Customer, CustomerRegistrationForm, ProductSizeForm
from django.contrib import messages
from django.shortcuts import get_object_or_404




# Create your views here.

def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())      
    
# class ProductDetail(View):
#     def get(self,request,pk):
#         product = Product.objects.get(pk=pk)
#         return render(request,"app/productdetail.html",locals())

# def product_detail(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     variations = Variation.objects.filter(product=product)
#     context = {
#         'product': product,
#         'variations': variations,
#     }
#     return render(request, 'product_detail.html', context)


# def product_detail(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     variations = Variation.objects.filter(product=product)
#     context = {
#         'product': product,
#         'variations': variations,
#     }
#     return render(request, 'product_detail.html', context)   



# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     size_chart = SizeChart.objects.all()
#     return render(request, 'product_detail.html', {'product': product, 'size_chart': size_chart})
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())    
    
class CustomerRegistrationView(View): 
    def get(self,request):  
        form= CustomerRegistrationForm()
        return render(request,"app/customerregistration.html",locals())
    def post(self,request):
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully")
        else:
            messages.warning(request,"Invalid data")
        return render(request,"app/customerregistration.html",locals())
    
def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()   
    return render(request,'app/contact.html')


class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request,"app/profile.html",locals())
    def post(self,request):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            user= request.user
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']    
            reg = Customer(user=user,name=name,address=address,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save() 
            messages.success(request,"Profile saved")
        else:
            messages.warning(request,"Invalid Data")
        return render(request,"app/profile.html",locals())
    
def address(request):
        add = Customer.objects.filter(user=request.user)
        return render(request,'app/address.html',locals())
    
class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'app/updateaddress.html',locals())
    def post(self,request,pk):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.address = form.cleaned_data['address']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Profile Updated")
        else:
            messages.warning(request,"Invalid data")
        return redirect('address')

# def add_to_cart(request):
#     user=request.user
#     product_id=request.GET.get('prod_id')
#     product= Product.objects.get(id=product_id)
#     Cart(user=user,product=product).save()
#     return redirect("/cart")


def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product= Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(product=product, user=request.user, ordered=False)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, "This item quantity was updated.")
    else:
        cart_item.quantity = 1
        cart_item.save()
        messages.success(request, "This item was added to your cart.") 
    return redirect('/cart')  

    # Cart(user=user,product=product).save()
    # return redirect("/cart")

def cart_add(request):
    cart = Cart(request)
    product_id = request.POST['product_id']
    product = get_object_or_404(Product, pk=product_id)
    size = request.POST['size']
    cart.add(product=product, size=size)
    return redirect('cart_detail')



def show_cart(request):
    user= request.user
    cart= Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity * p.product.selling_price
        amount=amount +value
    totalamount= amount+20    
    return render(request, 'app/addtocart.html',locals())
  
def plus_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1 
        c.save()     
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(prod_id)
        amount=0
        for p in cart:
            value=p.quantity * p.product.selling_price
            amount=amount +value
        totalamount= amount+20    
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
             
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1 
        c.save()     
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity * p.product.selling_price
            amount=amount +value
        totalamount= amount+20    
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount     
        }
        return JsonResponse(data)    
    
def remove_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user)) 
        c.delete()     
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value=p.quantity * p.product.selling_price
            amount=amount +value
        totalamount= amount+20    
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount     
        }
        return JsonResponse(data) 
  
# def size_chart(request):
#     size_chart = SizeChart.objects.all()
#     return render(request, 'size_chart.html', {'size_chart': size_chart})
# def add_to_cart(request):
#     if request.method == 'POST':
#         prod_id = request.POST.get('prod_id')
#         size = request.POST.get('size')
        # rest of the code for adding to cart goes here

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductSizeForm()
    return render(request, 'product_detail.html', {'product': product, 'form': form})

