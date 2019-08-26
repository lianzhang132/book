"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path,include
from book1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"search/",views.search,name="search"),
    re_path(r"authoradd/",views.authoradd,name="authoradd"),
    re_path(r"publicadd/",views.publicadd,name="publicadd"),
    re_path(r"bookadd/",views.bookadd,name="bookadd"),
    re_path(r"lists/",views.lists,name="lists"),
    re_path(r"booklist/",views.booklist,name="booklist"),
    re_path(r"bookdelete/(\d+)",views.bookdelete,name="bookdelete"),
    re_path(r"bookupdate/(\d+)",views.bookupdate,name="bookupdate"),
]
