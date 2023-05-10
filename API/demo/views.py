from django.shortcuts import render
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from demo.models import Weapon
from demo.serializers import WeaponSerializer

# @api_view(['GET', 'POST'])
# def demo(request):
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()
#         res = WeaponSerializer(weapons, many=True)
#         return Response(res.data)
#     if request.method == 'POST':
#         return Response({'status': 200})

#вместо выше изображенной функции используем специальный класс и не забываем его прописать в urls
# class DemoView(APIView):
#     def get(self, requst):
#         weapons = Weapon.objects.all()
#         res = WeaponSerializer(weapons, many=True)
#         return Response(res.data)
#
#     def post(self, request):
#         return Response({'status': 200})


class DemoView(ListAPIView):
    queryset = Weapon.objects.all()#откуда берем данные
    serializer_class = WeaponSerializer#с помощью чего превращаем в json - serializers

    def post(self, request):
        return Response({'status': 200})
