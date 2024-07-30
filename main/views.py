from django.shortcuts import render
from vegitables.models import Vegitable, Fruit
from django.contrib.auth.decorators import login_required
from django.views import View

vegitables = Vegitable.objects.all()
fruits = Fruit.objects.all()

# Create your views here.
# def index_view(request):
#     return render(request, 'index.html', context={'vegitables':vegitables, 'fruits':fruits})

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', context={'vegitables':vegitables, 'fruits':fruits})
        

# def base_view(request):
#     # if request.method == "POST":
#     #     search = request.POST['search']
#     #     if (Fruit.objects.filter(name__icontains=search) or Vegitable.objects.filter(name__icontains=search)):
#     #         fruits = Fruit.objects.filter(name__icontains=search)
#     #         vegitables = Vegitable.objects.filter(name__icontains=search)
#     #         return render(request, 'base.html', context={'fruits':fruits, 'vegitables':vegitables, 'message':'found'})        
#     #     return render(request, 'base.html', context={'message':'no'})    
#     if request.method == 'POST':
#         search = request.POST['search']
#         if (Vegitable.objects.filter(name__icontains=search) or Fruit.objects.filter(name__icontains=search)):
#             vegitables = Vegitable.objects.filter(name__icontains=search)
#             fruits = Fruit.objects.filter(name__icontains=search)
#             return render(request, 'base.html', context={'vegitables':vegitables, 'fruits':fruits, 'message':'found'})
#         return render(request, 'base.html', context={'message':'no'})
#     return render(request, 'base.html')

class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')
    
    def post(self, request):
        search = request.POST['search']
        if (Vegitable.objects.filter(name__icontains=search) or Fruit.objects.filter(name__icontains=search)):
            vegitables = Vegitable.objects.filter(name__icontains=search)
            fruits = Fruit.objects.filter(name__icontains=search)
            return render(request, 'base.html', context={'vegitables':vegitables, 'fruits':fruits, 'message':'found'})
        return render(request, 'base.html', context={'message':'no'})

# @login_required
# def cart_view(request):
#     product_name = request.GET.get('data')
#     product_names = []
#     product_names.append(product_name)
#     for product_name_for in product_names:
#         if Vegitable.objects.filter(name=product_name_for):
#             vegitables = Vegitable.objects.filter(name=product_name_for)
#             return render(request, 'cart.html', context={'products':vegitables})
#         fruits = Fruit.objects.filter(name=product_name_for)
#         return render(request, 'cart.html', context={'products':fruits})

# @login_required
class CartView(View):
    def get(self, request):
        product_name = request.GET.get('data')
        if Vegitable.objects.filter(name=product_name):
            vegitables = Vegitable.objects.filter(name=product_name)
            return render(request, 'cart.html', context={'products':vegitables})
        fruits = Fruit.objects.filter(name=product_name)
        return render(request, 'cart.html', context={'products':fruits})

# def chackout_view(request):
#     return render(request, 'chackout.html', context={'vegitables':vegitables, 'fruits':fruits})

class ChackOutView(View):
    def get(self, request):
        return render(request, 'chackout.html', context={'vegitables':vegitables, 'fruits':fruits})

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

def shop_detail_view(request, name):
    if request.method == 'POST':
        if Vegitable.objects.filter(name=name):
            product = Vegitable.objects.get(name=name)
            product.delete()
            return render(request,'shop.html', context={'vegitables':vegitables, 'fruits':fruits})
        product = Fruit.objects.filter(name=name)
        product.delete()
        return render(request, 'shop.html', context={'vegitables':vegitables, 'fruits':fruits})
    
    if Vegitable.objects.filter(name=name):
        vegitable = Vegitable.objects.get(name=name)
        return render(request, 'shop_detail.html', context={'product':vegitable, 'vegitables':vegitables, 'fruits':fruits})
    fruit = Fruit.objects.get(name=name)
    return render(request, 'shop_detail.html', context={'product':fruit, 'vegitables':vegitables, 'fruits':fruits})

class ShopView(View):
    def get(self, request):
        return render(request, 'shop.html', context={'vegitables':vegitables, 'fruits':fruits})

class TestimonialView(View):
    def get(self, request):
        return render(request, 'testimonial.html')

class ErrorView(View):
    def get(self, request):
        return render(request, '404.html')