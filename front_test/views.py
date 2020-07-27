from django.shortcuts import render, redirect
from django.conf import settings
from scheduler import insert_observation_post_schedule

def signup(request):
    return render(request, 'front_test/signup.html')

def login(request):
    return render(request, 'front_test/login.html')

def menu(request):
    if request.session.get('email', False):
        static_root = settings.STATIC_ROOT_WEB
        session_email = request.session['email']
        session_id = request.session['_auth_user_id']
        print('login user : ' + session_email)
        return render(request, 'front_test/menu.html', \
        {'static_root':static_root, 'session_email':session_email, 'session_id':session_id})
    else:
        return redirect('/front/login/')

def map(request):
    if request.session.get('email', False):
        static_root = settings.STATIC_ROOT_WEB
        app_key = settings.KAKAO_JAVASCRIPT_APP_KEY
        return render(request, 'front_test/map.html', {'static_root':static_root, 'app_key': app_key})
    else:
        return redirect('/front/login/')

def dive_log_list(request):
    if request.session.get('email', False):
        static_root = settings.STATIC_ROOT_WEB
        return render(request, 'front_test/diveloglist.html', {'static_root':static_root})
    else:
        return redirect('/front/login/')

def dive_log_form(request):
    if request.session.get('email', False):
        static_root = settings.STATIC_ROOT_WEB
        return render(request, 'front_test/divelogform.html', {'static_root':static_root})
    else:
        return redirect('/front/login/')

def update_obs(request):
    insert_observation_post_schedule()
    return redirect('/front/map/')
