"""
URL configuration for library project.

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
from books import views
app_name='books'
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('view',views.view,name='view'),
    path('factorial',views.factorial,name='factorial'),
    path('detailview/<int:i>',views.detailview,name='detailview'),
    path('deletebook/<int:i>',views.deletebook,name='deletebook'),
    path('edit/<int:i>',views.edit,name="edit"),
    path('search',views.search,name="search"),
]
