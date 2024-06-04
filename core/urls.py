"""core URL Configuration

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
from django.urls import path,re_path,include
# from allauth.account.views import confirm_email

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/auth/', include('djoser.urls')),
    re_path(r'^api/auth/', include('djoser.urls.jwt')),
    # re_path(r'^accounts/', include('allauth.urls')),
    # re_path(r'^rest-auth/', include('rest_auth.urls')),
    # re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('rest_framework.urls')),
    re_path(r'^api/', include('users.urls')),

    # re_path(r'^accounts/', include('allauth.urls')),
    # re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]
