from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,blank=True)

    def save(self , *args, **kwargs):
        self.slug=slugify(self.category_name)     # django save method is override
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name                 # save by category name


class Sub_Category(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ColorVariant(models.Model):                     #class for different color variant
    color_name=models.CharField(max_length=100)   
    color_code=models.CharField(max_length=100)
    def __str__(self):
        return self.color_name                     # save by color name

class QuantityVariant(models.Model):                  #class for different Quantity variant
    varient_name=models.CharField(max_length=100)
    def __str__(self):
        return self.varient_name                   # save by varient name

class SizeVariant(models.Model):                      #class for different size variant
    size_name=models.CharField(max_length=100)
    def __str__(self):
        return self.size_name                      # save by size name


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default='') # on_delete=models.CASCADE: Related product also gets deleted
    sub_category=models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False,default='')
    product_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='static/products')
    price=models.CharField(max_length=20)
    decription=models.TextField()
    stock=models.IntegerField(default=100)

    quantity_type=models.ForeignKey(QuantityVariant, blank=True,null=True,on_delete=models.PROTECT)
    color_type=models.ForeignKey(ColorVariant, blank=True,null=True,on_delete=models.PROTECT)
    size_type=models.ForeignKey(SizeVariant, blank=True,null=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.product_name                # save by product name