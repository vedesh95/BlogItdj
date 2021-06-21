"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from project import views
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('admin/', admin.site.urls),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout"),
    path('singleblog/<int:id>/',views.singleblog,name="singleblog"),
    path('blog',views.blog,name="blog"),
    path('categoryblogs/<str:category>/',views.categoryblogs,name="categoryblogs"),
]

