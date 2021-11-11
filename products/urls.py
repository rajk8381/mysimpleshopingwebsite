
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('new/', views.new_user),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('details/<pid>/', views.details), # ,id get karne ke liye <id> variable create karna
    path('editpro/<id>/', views.product_edit), # ,id get karne ke liye <id> variable create karna
]


# def myfun(request,pid=None):
#     pass
#
# myfun("details/1")
