from rest_framework import serializers
from allauth.account.adapter import get_adapter
from .models import User
from django.db import transaction
from allauth.account.utils import setup_user_email
from rolepermissions.roles import assign_role
from dj_rest_auth.registration.serializers import RegisterSerializer
from users.models import GENDER_SELECTION,ROLES

class RegisterSerializer(RegisterSerializer):
    gender = serializers.ChoiceField(choices=GENDER_SELECTION)
    phone_number = serializers.CharField(max_length=30)
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.gender = self.data.get('gender')
        user.phone_number = self.data.get('phone_number')
        user.save()
        user.role=assign_role(user,'user')
        user.save()
        return user

class UserDetailsSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name',
                  'last_name', 'address', 'city', 'about_me', 'profile_image' ,'phone_number','role','gender')
        read_only_fields = ('email', )