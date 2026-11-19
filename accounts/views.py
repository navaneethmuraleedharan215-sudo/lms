from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import UserSerializer,TrainerprofileSerializer,StudentprofileSerializer
from accounts.models import User,TrainerProfile,StudentProfile
from rest_framework.response import Response
from rest_framework import authentication,permissions
from accounts.permissions import IsTrainer
# Create your views here.

class UserCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=User.objects.create_superuser(role="admin",**cleaned_data)
            serializer_instance=UserSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class StudentcreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=User.objects.create_user(role="student",**cleaned_data)
            serializer_instance=UserSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TrainercreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            instance=User.objects.create_user(role="trainer",**cleaned_data)
            serializer_instance=UserSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TrainerDetailView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsTrainer]

    def get(self,request):
        instance=request.user.trainer
        serializer=TrainerprofileSerializer(instance)
        return Response(data=serializer.data)

class TrainerUpdateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated,IsTrainer]

    def put(self,request,pk=None):
        form_data=request.data
        instance=request.user.trainer
        serializer=TrainerprofileSerializer(data=form_data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)