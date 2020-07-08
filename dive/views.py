import json
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DivePointSerializer, DiveLogSerializer
from .models import DivePoint, DiveLog

class DivePointViewSet(viewsets.ModelViewSet):
    serializer_class = DivePointSerializer
    queryset = DivePoint.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('diver',)

point_list = DivePointViewSet.as_view({
    'get': 'list',
    'post': 'create',
    })

class DiveLogViewSet(viewsets.ModelViewSet):
    serializer_class = DiveLogSerializer
    queryset = DiveLog.objects.all()

@api_view(['GET'])
def dive_point(request):
    if request.method == 'GET':
        d = DivePoint()
        d._create_point_id('1')
        queryset = DivePoint.objects.all()
        serializer_class = DivePointSerializer(queryset, many=True)
        return Response(serializer_class.data)

class DivePointView(APIView):
    def get(self, request):
        queryset = DivePoint.objects.all()
        serializer_class = DivePointSerializer(queryset, many=True)
        return Response(serializer_class.data)
