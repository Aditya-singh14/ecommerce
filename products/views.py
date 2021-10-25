from django.shortcuts import render
from products.models import Category
# Create your views here.

def index(request):
    category =Category.objects.all()
    context={
        'category':category,
    }
    return render(request,'index.html',context)