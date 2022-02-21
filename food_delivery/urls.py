"""food_delivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from os import remove
from django.contrib import admin
from django.urls import path
from core.views import base, about, search, cart, removeCart, addCard, signup, signin, signout, product, order
from food_delivery.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('', base, name='base'),
    path('admin/', admin.site.urls),
    path('about', about, name='about'),
    path('search', search, name='search'),
    
    path('addCard/<int:id>', addCard, name='addCard'),
    path('cart', cart, name='cart'),
    path('removeCart/<int:id>', removeCart, name='removeCart'),

    path('signup', signup, name='signup'),  # регизстрация
    path('signin', signin, name='signin'),  #войти
    path('signout', signout, name='signout'), #выйти
    path('product/<int:id>', product, name='product'),
    path('order', order, name='order'),
]

# urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
