from django.shortcuts import render, redirect
from django.conf import settings
from scheduler import insert_observation_post_schedule

def signup(request):
    return render(request, 'front_test/signup.html')

def login(request):
    return render(request, 'front_test/login.html')

def menu(request):
    if request.session.get('email', False):
        session_email = request.session['email']
        session_id = request.session['_auth_user_id']
        print('login user : ' + session_email)
        return render(request, 'front_test/menu.html', \
        {'session_email':session_email, 'session_id':session_id})
    else:
        return redirect('/front/login/')

def change_profile(request):
    if request.session.get('email', False):
        return render(request, 'front_test/change_profile.html')
    else:
        return redirect('/front/login/')

def map(request):
    if request.session.get('email', False):
        app_key = settings.KAKAO_JAVASCRIPT_APP_KEY
        return render(request, 'front_test/map.html', {'app_key': app_key})
    else:
        return redirect('/front/login/')

def dive_log_list(request):
    if request.session.get('email', False):
        return render(request, 'front_test/diveloglist.html')
    else:
        return redirect('/front/login/')

def dive_log_form(request):
    if request.session.get('email', False):
        return render(request, 'front_test/divelogform.html')
    else:
        return redirect('/front/login/')

def update_obs(request):
    insert_observation_post_schedule()
    return redirect('/front/map/')
