"""backendEtech URL Configuration

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
from django.urls import path , include
from rest_framework import permissions # 2
from dj_rest_auth.registration.views import VerifyEmailView,ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new
schema_view = get_schema_view( # new
openapi.Info(
title="Blog API",
default_version="v1",
description="Here is the blog for Etech-Sw ",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="info@etech-sw.org "),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health',include('blog.urls'),name='health'),
    
     path(
        'api/user/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ), #6 before registration
    path('api-auth/', include('rest_framework.urls')),#1
    path('api/user/', include('dj_rest_auth.urls')), #3
    path('user/api/' ,include('users.urls')),
    path('blog/api/' ,include('blog.urls') , name='blog'),
    path('api/user/registration/', include('dj_rest_auth.registration.urls')),#4
    path('api/user/account-confirm-email/',VerifyEmailView.as_view(),name='account_email_verification_sent'),#5
   path(
        'rest-auth/password/reset/confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),#6
   path('swagger/', schema_view.with_ui( # new
'swagger', cache_timeout=0), name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui( # new
'redoc', cache_timeout=0), name='schema-redoc'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
