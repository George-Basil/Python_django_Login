from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.user_login,),
    path('home/',views.home, name='home'),
    path('user_logout/', views.user_logout, name='user_logout')
    
] 