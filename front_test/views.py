from django.shortcuts import render
from django.conf import settings

def show_map(request):
    app_key = settings.KAKAO_JAVASCRIPT_APP_KEY
    return render(request, 'front_test/map.html', {'app_key': app_key})

def show_login(request):
    return render(request, 'front_test/login.html')

def show_menu(request):
    if request.session['_auth_user_id']:
        print('login user : {}'.format(request.session['_auth_user_id']))
        return render(request, 'front_test/menu.html')
    else:
        return render(request, 'front_test/login.html')
