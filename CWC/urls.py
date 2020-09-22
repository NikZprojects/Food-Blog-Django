"""CWC URL Configuration

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
from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='blog'),
    path('about/', about_view, name='blog'),
    path('privacy_policy/', privacy_policy_view, name='blog'),
    path('recipes/', all_recipes_view, name='blog'),
    path('recipes/avocado_toast/', avocado_toast_view, name='blog'),
    path('recipes/banana_bread/', banana_bread_view, name='blog'),
    path('recipes/banana_bread_overnight_oats/', banana_bread_overnight_oats_view, name='blog'),
    path('recipes/breakfast_sandwich/', breakfast_sandwich_view, name='blog'),
    path('recipes/cookie_dough_cupcakes/', cookie_dough_cupcakes_view, name='blog'),
    path('recipes/lemon_chicken/', lemon_chicken_view, name='blog'),
    path('recipes/sweet_cream_cold_brew/', sweet_cream_cold_brew_view, name='blog'),
    path('experiments/', experiments_view, name='blog'),
    path('experiments/edible_cookie_dough/', edible_cookie_dough_view, name='blog'),
    path('experiments/homemade_grape_jam/', homemade_grape_jam_view, name='blog'),
    path('sitemap.xml', site_map_view, name='blog'),
    path('robots.txt', robots_txt_view, name='blog'),
]

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'
# handler403 = 'permission_denied_view'
# handler400 = 'bad_request_view'
