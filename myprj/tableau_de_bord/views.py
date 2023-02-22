from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'tableau_de_bord/index.html')

def staff(request):
    return render(request, 'tableau_de_bord/staff.html')

def product(request):
    return render(request, 'tableau_de_bord/product.html')

def order(request):
    return render(request, 'tableau_de_bord/order.html')

