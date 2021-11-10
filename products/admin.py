from django.contrib import admin

# Register your models here.
from products.models import Product,MainCat,SubCat
# from .models import Product
# register alag alg hi karna hoga

admin.site.register(Product)
admin.site.register(MainCat)
admin.site.register(SubCat)
