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
def signup_view(request):
    user = User.objects.create_user(email=request.data['email'], \
    password=request.data['password'], nickname=request.data['nickname'], \
    profile_image=request.FILES.get('profile_image', default='profile/default.JPG'), \
    license_image=request.FILES.get('license_image', default='license/default.JPG'))
    print('signup - [{}]'.format(user.get_email))
    return redirect('/front/login/')

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        user = authenticate(email=request.data['email'], password=request.data['password'])
        if user is not None:
            login(request, user)
            request.session['email'] = request.data['email']
            return redirect('/front/menu/')
        else:
            return Response('실패')

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return redirect('/front/login/')
