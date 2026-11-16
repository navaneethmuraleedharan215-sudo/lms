from rest_framework import serializers
from accounts.models import User,StudentProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model=User

        fields=["id","username","email","password","phone","role"]

class StudentprofileSerializer(serializers.ModelSerializer):

    class Meta:

        model=StudentProfile

        fields="__all__"

        read_only_fields=["id","student"]