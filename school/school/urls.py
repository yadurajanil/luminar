"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from schoolapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('add',views.Addschool.as_view(),name="add"),
path('addstu',views.Addstudent.as_view(),name="addstu"),
path('listschool',views.Schoollist.as_view(),name="listschool"),
path('detail/<int:pk>',views.Schooldetail.as_view(),name="detail"),
path('studetail',views.Studentdetail.as_view(),name="studetail"),
path('register',views.Register.as_view(),name="register"),
path('login',views.Login.as_view(),name="login"),
path('logout',views.Logout.as_view(),name="logout"),
]
