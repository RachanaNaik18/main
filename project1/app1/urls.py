from django.urls import path
from app1 import views

urlpatterns =[
    path("home/", views.home, name="home"),
    path('enter/', views.data, name="enter"),
    path("update/<int:id>", views.update, name="update"),
    path("<int:id>", views.dele, name="dele"),
    path('cart/', views.cart, name='cart'),
    path('addtocart/', views.add_to_cart, name='addtocart')
]