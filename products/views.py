from django.shortcuts import render
from products.models import *
# Create your views here.

def index(request):
    category =Category.objects.all()
    product =Product.objects.all()
    # sub_category=Sub_Category.objects.all()
    context={
        'category':category,
        'product':product,
        # 'sub_category':sub_category
    }
    return render(request,'index.html',context)