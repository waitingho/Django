"""ShoppingCart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shopping.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$/', index, name="index"),
    url(r'^index/$', index, name="index"),
    url(r'^update_item/$', update_item_quantity, name="update_item_quantity"),
    url(r'^thankyou/$', thank_you, name="thank_you"),
    url(r'^confirm_order/$', confirm_order, name="confirm_order"),
    url(r'^remove_item/$', remove_item, name="remove_item"),
    url(r'^cart/$', cart, name="cart"),
    url(r'^credit_card_page/$', credit_card_page, name="credit_card"),
    url(r'^add_to_cart/$', add_to_cart, name="add_to_cart"),
]
