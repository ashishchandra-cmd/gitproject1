"""regproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_views ,name='home_views'),
    path('regist/', views.register_views ,name='register_views'),
    path('admins/', views.admins_views,name='admins_show'),

    path('strocker/', views.strocker_views,name='strocker_show'),
    path('dispatcher/', views.dispatcher_views,name='dispatcher_show'),
    path('customer/', views.customer_views,name='customer_show'),




    path('login/', views.login_view, name='login_name'),
    path('user_login/', views.user_login_view, name='user_login'),
    path('user_logout/', views.logout_view, name='user_logout_name'),


    path('customerRegister/',views.customerRegister, name='customerRegister_show')
]
