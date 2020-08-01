from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from .models import ObservationPost
from .serializers import ObservationPostSerializer
from third_party_api import KakaoApi, KhoaApi

@api_view(['GET'])
def observation_post(requset):
    queryset = ObservationPost.objects.all()
    serializer_class = ObservationPostSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data, safe=False)

@api_view(['GET'])
def sea_state(request):
    khoa_api = KhoaApi()
    obs_code = request.GET['obscode']    # DT_0010
    res = khoa_api.khoa_get_sea_state(obs_code)
    return JsonResponse(res.json())

@api_view(['GET'])
def region_code(request):
    kakao_api = KakaoApi()
    longitude = request.GET['longitude']
    latitude = request.GET['latitude']
    res = kakao_api.kakao_get_region_code(longitude, latitude)
    return JsonResponse(res.json())
