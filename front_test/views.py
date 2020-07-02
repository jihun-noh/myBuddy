from django.shortcuts import render
from django.conf import settings

def show_map(request):
    app_key = settings.KAKAO_JAVASCRIPT_APP_KEY
    return render(request, 'front_test/map.html', {'app_key': app_key})
