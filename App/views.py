from django.shortcuts import render
from .models import ProductMst, ProductSubCategory

def home(request):
    return render(request, 'products/home.html')

def product_list(request):
    products = ProductSubCategory.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def search_product(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = ProductSubCategory.objects.filter(product__product_name__icontains=query)
    return render(request, 'products/search_results.html', {'results': results})
