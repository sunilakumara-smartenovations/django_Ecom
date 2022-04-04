from django.urls import path
from . import views
urlpatterns =[
    path('saveenquiry/',views.saveEnquiry,name="saveenquiry"),

    #path('add',views.add,name='add')
]
