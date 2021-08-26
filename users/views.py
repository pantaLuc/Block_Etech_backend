from typing_extensions import ParamSpecArgs
from rest_framework import viewsets
from users.serializers import UserDetailsSerializer
from django.shortcuts import render
from .models import User

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from dj_rest_auth.social_serializers import TwitterLoginSerializer
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rolepermissions.roles import assign_role , get_user_roles

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter



class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    #callback_url = CALLBACK_URL_YOU_SET_ON_GITHUB
    client_class = OAuth2Client

class changeUserRole(viewsets.ViewSet):

    def change_user_role_to_admin(self ,request ,pk):
        user=User.objects.get(id=pk)
        if user.role !='user' or user.role!='writer':
            assign_role(user ,'admin')
            user.role='admin'
            user.save()
        else :
            pass

