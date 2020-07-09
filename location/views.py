from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from .models import ObservationPost
from .serializers import ObservationPostSerializer
from third_party_api import KakaoApi, KhoaApi

class ObservationPostViewSet(viewsets.ModelViewSet):
    serializer_class = ObservationPostSerializer
    queryset = ObservationPost.objects.all()

@api_view(['GET'])
def sea_state(request):
    khoa_api = KhoaApi()
    obs_code = request.GET['obscode']    # DT_0010
    res = khoa_api.khoa_get_sea_state(obs_code)
    return HttpResponse(res)

@api_view(['GET'])
def region_code(request):
    kakao_api = KakaoApi()
    longitude = request.GET['longitude']
    latitude = request.GET['latitude']
    res = kakao_api.kakao_get_region_code(longitude, latitude)
    return HttpResponse(res)
