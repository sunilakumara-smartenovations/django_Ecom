from django.urls import path
from . import views
urlpatterns =[
    path('',views.index,name="index"),
    path('about/',views.about),
    path('fruit/', views.fruit),
    path('blog/', views.blog),
    path('contact/', views.contact),
    path('Shop_Now/', views.Shop_Now),
]
