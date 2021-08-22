from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import  FacebookLogin,TwitterLogin,GithubLogin
from dj_rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)


urlpatterns=[
   path('dj-rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
   path('facebook/', FacebookLogin.as_view(), name='fb_login'),
   path('dj-rest-auth/github/', GithubLogin.as_view(), name='github_login'),
    path(
        'socialaccounts/',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    path(
        'socialaccounts/<int:pk>/disconnect/',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect')
]