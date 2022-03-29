from django.shortcuts import render
from django.http import HttpResponse
from.models import product,slide01,slide02



# Create your views here.

def index(request):
    pros = product.objects.all()
    sdls1 = slide01.objects.all()
    sdls2 = slide02.objects.all()
    return render(request, 'index.html', {'pros': pros, 'sdls1':sdls1, 'sdls2':sdls2})



def fruit(request):
    pros = product.objects.all()
    return render(request, 'fruit.html', {'pros': pros})

def about(request):
    return render(request, 'about.html')
def fruit(request):
    return render(request, 'fruit.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def Shop_Now(request):
    return render(request, 'shop_checkout.html')

def MY_SHOP(request):
    return render(request, 'about.html')