"""
URL configuration for restaurant project.

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
from app1 import views
app_name = 'app1'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Display.as_view()),
    path('home', views.List.as_view(), name='home'),
    path('items/<int:pk>/',views.Detail.as_view(),name='items_detail'),
    path('add', views.Add.as_view(), name="add"),
    path('update/<int:pk>/', views.Update.as_view(), name="update"),

]