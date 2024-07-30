from django.shortcuts import render, redirect
from .forms import VegitableForm, FruitForm
from django.views import View

# Create your views here.
# def create_product_view(request):
#     # return render(request, 'create_product.html')
#     if request.method == 'POST':
#         data = request.GET.get('data')
#         print("cccccccccccccccccccccccccccccccccc", data)
#         if data == 'vegitables':
#             form = VegitableForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('shop')
#         form1 = FruitForm(request.POST)
#         if form1.is_valid():
#             form1.save()
#             return redirect('shop')
#     data = request.GET.get('data')
#     form = FruitForm(request.POST)
#     return render(request, 'create_product.html', context={'form': form, 'message':data})

class Create_ProductView(View):
    def get(self, request):
        data = request.GET.get('data')
        form = FruitForm(request.POST)
        return render(request, 'create_product.html', context={'form': form, 'message':data})

    def post(self, request):
        data = request.GET.get('data')
        if data == 'vegitables':
            form = VegitableForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('shop')
        form1 = FruitForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('shop')