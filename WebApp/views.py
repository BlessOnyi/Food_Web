from django.shortcuts import get_object_or_404, render
from .models import *


# Create your views here.



def myHome(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    # Check if a category is selected
    selected_category = request.GET.get('category')

    if selected_category:
        # Filter food items by the selected category
        products = Product.objects.filter(category__slug=selected_category)

    return render (request, 'index.html', {'products':products,'categories':categories})





def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'post_detail.html',{'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug =category_slug)
    products = Product.objects.filter(category=category)
    return render (request, 'category.html',{'category':category, 'products':products})



# def about(request):
#     return render (request, 'about.html')

# def menu(request):
#     return render (request, 'menu.html')

# def booking(request):
#     return render (request, 'book.html')