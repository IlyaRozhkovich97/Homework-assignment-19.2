from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def home_page(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'main/home_page.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f"\nСообщение из формы обратной связи:\n\033[91mИмя пользователя:\033[0m {name}\n\033[91mЭлектронная почта:"
            f"\033[0m {email}\n\033[91mТелефон:\033[0m {phone}\n\033[91mСообщение:\033[0m {message} ")
    return render(request, 'main/contacts.html')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'main/add_product.html', {'form': form})