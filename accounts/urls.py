from django.urls import path
from . import views



urlpatterns =[
    path('register/',views.register_view,name="register"),
    path('login/',views.login_view,name="login"),
    # path('logout',views.logout,name="logout"),
    #path('add',views.add,name='add')
]



# urlpatterns =[
#     path('register',views.register,name="register"),
#     path('login',views.login,name="login"),
#     path('logout',views.logout,name="logout"),
#     #path('add',views.add,name='add')
# ]
