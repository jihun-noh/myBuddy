from django.shortcuts import render, redirect
from django.conf import settings

def show_map(request):
    if request.session.get('email', False):
        session_email = request.session['email']
        session_id = request.session['_auth_user_id']
        app_key = settings.KAKAO_JAVASCRIPT_APP_KEY
        return render(request, 'front_test/map.html', \
        {'app_key': app_key, 'session_email':session_email, 'session_id':session_id})
    else:
        return redirect('/front/login/')

def show_login(request):
    return render(request, 'front_test/login.html')

def show_menu(request):
    if request.session.get('email', False):
        session_email = request.session['email']
        print('login user : ' + session_email)
        return render(request, 'front_test/menu.html', {'session_email': session_email})
    else:
        return render(request, 'front_test/login.html')

def show_signup(request):
    return render(request, 'front_test/signup.html')
