"""jbfullstackframeworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from accounts import urls as accounts_urls
from accounts.views import index
from products import urls as urls_products
from search import urls as urls_search
from checkout import urls as urls_checkout
from cart import urls as urls_cart
from sendemail import urls as urls_sendemail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(accounts_urls, namespace=None)),
    url(r'^products/', include(urls_products, namespace=None)),
    url(r'^cart/', include(urls_cart, namespace=None)),
    url(r'^search/', include(urls_search, namespace=None)),
    url(r'^checkout/', include(urls_checkout, namespace=None)),
    url(r'^contact/', include(urls_sendemail, namespace=None)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]
