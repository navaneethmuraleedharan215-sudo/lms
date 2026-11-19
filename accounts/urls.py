from django.contrib import admin
from django.urls import path,include
from accounts.views import TrainercreateView,StudentcreateView,UserCreateView,TrainerDetailView
from accounts.views import TrainerUpdateView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[
    path('trainer/register/',TrainercreateView.as_view()),
    path('student/register/',StudentcreateView.as_view()),

    path('trainer/token/',ObtainAuthToken.as_view()),
    path('profile/me/',TrainerDetailView.as_view()),
    path('profile/complete/',TrainerUpdateView.as_view()),
]