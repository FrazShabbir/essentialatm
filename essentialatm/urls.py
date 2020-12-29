""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.signin,name="signin"),
    path('sign-up/', views.signup,name="signup"),
    path('sign-in/', views.signin,name="signin"),
    path('home/', views.index,name="index"),

    path('sign-out/', views.logout,name="logout"),
    path('inputamount/', views.amount,name="amount"),
    path('totalbalance/', views.balanceinq,name="balanceinq"),
    path('gethelp/', views.gethelp,name="gethelp"),
    path('quickamount/', views.quickamount,name="quickamount"),
    path('checkout/', views.checkout,name="checkout"),
    path('quickamount/baltenk/', views.baltenk,name="baltenk"),
    path('quickamount/balfivek/', views.balfivek,name="balfivek"),
    path('quickamount/balfifk/', views.balfifk,name="balfifk"),
    path('quickamount/baltwk/', views.baltwk,name="baltwk"),
]
