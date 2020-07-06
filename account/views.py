from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

@api_view(['POST'])
def signup(request):
    user = User.objects.create_user(email=request.data['email'], \
    password=request.data['password'], nickname=request.data['nickname'])
    return user

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is not None:
            login(request, user)            
            return redirect('/front/menu/')
        else:
            return Response('실패')

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return Response('로그아웃')
