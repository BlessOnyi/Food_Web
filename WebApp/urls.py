from django.urls import path
from . import views


app_name ='WebApp'
urlpatterns = [
    path('', views.myHome, name='myHome'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>', views.category_list, name='category_list'),
    # path('about', views.about, name='about'),
    # path('menu', views.menu, name='menu'),
    # path('booking', views.booking, name='booking'),   
]