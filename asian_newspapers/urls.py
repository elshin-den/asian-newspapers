"""asian_newspapers URL Configuration

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
from django.conf.urls import url
from main_app.views import main, contacts, newspapers, websites, newspaper_detail, banner_detail, price_list
from django.contrib import admin
from user_management_app.views import login, logout, registration
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', main, name='main_page'),
]

urlpatterns += [
    url(r'^user/login/$', login, name='login'),
    url(r'^user/logout/$', logout, name='logout'),
    url(r'^user/registration/$', registration, name='registration'),
    url(r'^contacts/$', contacts, name='contacts'),
    #url(r'^novikov/$', novikov, name='novikov'),
    url(r'^newspapers/$', newspapers, name='newspapers'),
    url(r'^websites/$', websites, name='websites'),
    url(r'^newspapers/(\d+)$', newspaper_detail, name='newspaper_detail'),
    url(r'^banners/(\d+)$', banner_detail, name='banner_detail'),
    url(r'^price_list/$', price_list, name='price_list'),
    url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='index')
]

#admin urls
urlpatterns += [
    url(r'^admin/', admin.site.urls),
]

'''urlpatterns += [
url(r'^admin/$', admin_page),
    url(r'^admin/delete/user/(\d+)/$', delete_user),
    url(r'^get_user_data/(\d+)/$', get_user),
    url(r'^admin/update_user_data/(\d+)/$', update_user),

    url(r'admin/categories/', admin_categories, name='admin_categories'),
    url(r'^admin/create/categories$', admin_categories_create, name='category_create'),
    url(r'^admin/delete/categories/(\d+)$', admin_categories_delete, name='category_delete'),
    url(r'^admin/update/categories/(\d+)$', admin_categories_update, name='category_update'),
    url(r'^admin/detail/categories/(\d+)$', admin_categories_detail, name='admin_category_detail')
]'''

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
