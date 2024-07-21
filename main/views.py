from django.shortcuts import render
from vegitables.models import Vegitable, Fruit

vegitables = Vegitable.objects.all()
fruits = Fruit.objects.all()

# Create your views here.
def index_view(request):
    return render(request, 'index.html', context={'vegitables':vegitables, 'fruits':fruits})

def base_view(request):
    # if request.method == "POST":
    #     search = request.POST['search']
    #     if (Fruit.objects.filter(name__icontains=search) or Vegitable.objects.filter(name__icontains=search)):
    #         fruits = Fruit.objects.filter(name__icontains=search)
    #         vegitables = Vegitable.objects.filter(name__icontains=search)
    #         return render(request, 'base.html', context={'fruits':fruits, 'vegitables':vegitables, 'message':'found'})        
    #     return render(request, 'base.html', context={'message':'no'})    
    if request.method == 'POST':
        search = request.POST['search']
        if (Vegitable.objects.filter(name__icontains=search) or Fruit.objects.filter(name__icontains=search)):
            vegitables = Vegitable.objects.filter(name__icontains=search)
            fruits = Fruit.objects.filter(name__icontains=search)
            return render(request, 'base.html', context={'vegitables':vegitables, 'fruits':fruits, 'message':'found'})
        return render(request, 'base.html', context={'message':'no'})
    return render(request, 'base.html')

def cart_view(request):
    product_name = request.GET.get('data')
    product_names = []
    product_names.append(product_name)
    for product_name_for in product_names:
        if Vegitable.objects.filter(name=product_name_for):
            vegitables = Vegitable.objects.filter(name=product_name_for)
            return render(request, 'cart.html', context={'products':vegitables})
        fruits = Fruit.objects.filter(name=product_name_for)
        return render(request, 'cart.html', context={'products':fruits})

def chackout_view(request):
    return render(request, 'chackout.html')

def contact_view(request):
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
    
    if request.method == 'POST':
        product_type = request.POST['']

def shop_view(request):
    return render(request, 'shop.html', context={'vegitables':vegitables, 'fruits':fruits})

def testimonial_view(request):
    return render(request, 'testimonial.html')

def error_view(request):
    return render(request, '404.html')