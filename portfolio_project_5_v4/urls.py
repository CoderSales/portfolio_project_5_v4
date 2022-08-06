"""portfolio_project_5_v4 URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404
# sitemap
# from django.contrib.sitemaps.views import sitemap
# from django.contrib import sitemaps
# # https://stackoverflow.com/questions/25220561/django-1-6-
# # name-sitemaps-is-not-defined
# from sitemaps import StaticViewSitemap


# sitemaps = {
#     'static': StaticViewSitemap
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('contact/', include('contact.urls')),
    path('todo/', include('todo.urls')),
    # path('sitemap.xml', sitemap,
    #      {'sitemaps': sitemaps},
    #      name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'portfolio_project_5_v4.views.handler404'  # noqa: F811,E501
