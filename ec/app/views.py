# from urllib import request
# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.db.models import Q
from django.shortcuts import render,redirect
from django.views import View
from requests import request
from . models import Product,Cart, Contact, Size,Wishlist
from .forms import CustomerProfileForm,Customer, CustomerRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
# from django.contrib.auth.views import LoginView


# Create your views here.
  


def home(request):
    return render(request,"app/home.html")

def about(request):
    # totalitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user=request.user))
    return render(request,"app/about.html",locals())

def contact(request):
    return render(request,"app/contact.html",locals())

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
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        return render(request,"app/productdetail.html",locals())
    
# class CustomLoginView(LoginView):
#     def get(self):
#         return render(request,"app/contact.html",locals())    

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
 

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request,"app/profile.html",locals())

    def post(self,request):
        form= CustomerProfileForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            user= request.user
            reg = Customer(user=user,name=name,address=address,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Profile saved")
            form = CustomerProfileForm() # reset form
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


class DeleteAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        add.delete()
        # messages.success(request, "Address deleted")
        return redirect('address')



def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    size_id = request.GET.get('size')
    product = Product.objects.get(id=product_id)
    if size_id:
        try:
            size = Size.objects.get(id=size_id)
        except Size.DoesNotExist:
            return HttpResponse("Invalid size.")
    else:
        # Assign a default size value if no size is provided
        size = Size.objects.get(size='N/A')
    # Check if there are any existing cart items for the user, product, and size
    cart_items = Cart.objects.filter(user=user, product=product, size=size, ordered=False)
    
    product = Product.objects.get(id=product_id)
    if cart_items.exists():
        # If cart item(s) already exist, update the quantity of the first item
        cart_item = cart_items.first()
        cart_item.quantity += 1
        cart_item.save()
    else:
        # If no cart item exists, create a new one
        cart_item = Cart.objects.create(user=user, product=product, size=size, quantity=1, ordered=False)
    
    return redirect('/cart')





def show_cart(request):
    user= request.user
    cart= Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value=p.quantity * p.product.selling_price
        amount=amount +value
    totalamount= amount+20    
    return render(request, 'app/addtocart.html',locals())



class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value = p.quantity * p.product.selling_price
            famount = famount +value
        totalamount = famount + 20    
        return render(request, 'app/checkout.html',locals())




    
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity + 1 > c.product.stock:
            return JsonResponse('Product quantity exceeds stock limit.')
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.selling_price
            amount = amount + value
        totalamount = amount + 20
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

    
def minus_cart(request):
    if request.method =='GET':
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity > 1:
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





def all_products(request):
    products = Product.objects.all()
    return render(request, 'app/all_products.html', {'products': products})    

  
def plus_wishlist(request):
    if request.method=='GET':
        prod_id=request.Get['prod_id']
        product=Product.objects.get(id=prod_id)
        user =request.user
        Wishlist(user=user,product=product).save()
        data={
            'message':'Wishlist Added Successfully',
        }
        return JsonResponse(data)



def minus_wishlist(request):
    if request.method=='GET':
        prod_id=request.Get['prod_id']
        product=Product.objects.get(id=prod_id)
        user =request.user
        Wishlist.objects.filter(user=user,product=product).delete()
        data={
            'message':'Wishlist Remove Successfully',
        }
        return JsonResponse(data)
