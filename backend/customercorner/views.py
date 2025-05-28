from django.shortcuts import render
from django.views.generic import DetailView, ListView , CreateView , DeleteView , TemplateView

from .models import Product, Product_type


class AllProductList(ListView):
    model = Product
    template_name = 'customercorner/all_products.html'
    context_object_name = 'all_products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'customercorner/product_detail.html'
    context_object_name = 'product' #will provide the class object with data and can be accessed with the help of the dot operator

class ProductCreateView(CreateView):
    model = Product
    template_name = 'customercorner/create_product.html'
    success_url = '/all_products/'
    context_object_name = 'form'
    fields = '__all__'


class Categories(ListView):
    model = Product_type
    template_name = 'customercorner/categories.html'
    context_object_name = 'categories'

def category_products_list(request,pk):
    data = Product_type.objects.get(id=pk)
    context = {'all_products' : data}
    return (request,'customercorner/category_products.html',context)
