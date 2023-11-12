from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, UserSignupSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
