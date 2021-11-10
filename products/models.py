from django.db import models

# Create your models here.

class MainCat(models.Model):
    name= models.CharField(max_length=100)
    # electrnic,fashion,mens,women

    def __str__(self):
        return self.name

class SubCat(models.Model):
    maincat=models.ForeignKey(MainCat, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    #mobile,laptop,airphone,Tv
    # shoes,belt,parse
    def __str__(self):
        return self.name
    #

class Product(models.Model):
    pro_image=models.ImageField(upload_to="products",default="p.png",
                                verbose_name="Product Image")
    pro_name=models.CharField("Product Name", max_length=200)
    desc=models.TextField("Description")
    price=models.DecimalField(decimal_places=2,max_digits=8) # 99999999.30
    datetime=models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=True)

    def __str__(self):
        return self.pro_name

    # pip install pillow
    # work on image
    # pip install -r req.txt

    # jab bhi hm image upload karenge to hame media ki settin karni padegi
    #follow rules in django
    # search on google "django media setting"
    # link https://stackoverflow.com/questions/5517950/django-media-url-and-media-root

    # project/urls.py
    # from django.conf import settings
    # from django.conf.urls.static import static
    #
    # urlpatterns=[
    #
    # ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # project/setting.py
    # import os
    # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # MEDIA_URL = '/media/'






