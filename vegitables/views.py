from django.shortcuts import render, redirect
from .forms import VegitableForm, FruitForm

# Create your views here.
def create_product_view(request):
    # return render(request, 'create_product.html')
    if request.method == 'POST':
        form = VegitableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
        # form1 = FruitForm(request.POST)
        # form1.is_valid()
        # form1.save()
        # return redirect('shop')
    form = FruitForm(request.POST)
    return render(request, 'create_product.html', {'form': form})
