from django.shortcuts import render,redirect
# select * from product
# ORM
# Product.objects.all() # Queryset[]
# Product.objects.filter() # Queryset[]

# Create your views here.
from .models import Product,MainCat,SubCat
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')


    p = Product.objects.all()
    if "skey" in request.GET:
        serkey=request.GET.get('skey')
        p=p.filter(pro_name__startswith=serkey)
    mydict={}
    maincat=MainCat.objects.all()
    subcat=SubCat.objects.all()

    mydict['records']=p
    mydict['maincat']=maincat
    mydict['subcat']=subcat

    return render(request,'home.html',mydict)

def details(request,pid=None):
    mydict={}
    p =Product.objects.get(id=pid)
    mydict['p']=p
    return render(request,'pro_details.html',mydict)

from django.contrib.auth.models import User
def new_user(request):
    mydict={}
    if request.method=="POST":
        uname =request.POST.get('uname')
        passw =request.POST.get('passw')
        email =request.POST.get('email')
        first_name =request.POST.get('first_name')
        rpassw =request.POST.get('rpassw')
        if len(passw)<8:
            mydict['error']="Password Must be 8 charector"
        elif(passw!=rpassw):
            mydict['error'] = "Password No Match"
        else:
            u=User.objects.create_user(username=uname,email=email,password=passw)
            if u:
                u.first_name=first_name
                u.last_name="Sharma"
                u.save()
                mydict['error'] = "New User Created"
            print(uname,passw,rpassw)

    return render(request,'new_user.html',mydict)

from django.contrib.auth import authenticate,login,logout
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    mydict={}
    if request.method=="POST":
        username1 =request.POST.get('uname')
        password1 =request.POST.get('passw')
        u =authenticate(username=username1,password=password1)
        if u:
            login(request,u)
            return redirect('/')
        else:
            mydict['error'] ="Username and Password invalid"
            print("user name not match")
    return render(request,'login.html',mydict)


def logout_view(request):
    logout(request)
    return redirect('login')


def product_edit(request,id=None):
    mydict={}
    p =Product.objects.get(pk=id)
    mydict['p']=p

    if request.method=="POST":
        image =request.FILES.get('image')
        pname =request.POST.get('pname')
        print(image.name.endswith(".jpg") or image.name.endswith(".png"))

        p =Product.objects.get(pk=id)
        p.pro_name=pname
        p.pro_image=image
        p.save()

        # Product.objects.filter(pk=id).update(pro_name=pname,pro_image=image)

        return redirect('/')


    return render(request,'editpro.html',mydict)