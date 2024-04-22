"""
URL configuration for oee_calculation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import views

urlpatterns = [
    path('machineview',views.mdisplay.as_view()),
    path('production_view',views.product_display.as_view()),
    path('',views.index),



    path('machine_update',views.machine_update),
    path('machine_get',views.machine_get),
    path('machine_s',views.machine_s),
    path('product_udt',views.product_udt),
    path('OEE_CALCULATION',views.OEE_CALCULATION),
    path('oee_informs',views.oee_info.as_view()),





    #path('good_product_count',views.good_product_count),

]
