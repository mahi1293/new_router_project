from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.authentication import BasicAuthentication


# from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from ajax_api.models import IP_Address
from .serializer import IpAddressSerializers
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from django.shortcuts import redirect, render, get_object_or_404, reverse


class IPAddressView(ListCreateAPIView):
    queryset = IP_Address.objects.all()
    serializer_class = IpAddressSerializers

    # def perform_create(self, serializer):
    #     print("query syey", self.request.data.get('id'))

    #     ipaddress = get_object_or_404(IP_Address, id=self.request.data.get('id'))
    #     # print("iparess", ipaddress)
    #     return serializer.save(ipaddress=ipaddress)


class IPViewSet(CreateAPIView):
    queryset = IP_Address.objects.all()
    serializer_class = IpAddressSerializers

# class SingleArticleView(RetrieveAPIView):
#     queryset = IP_Address.objects.all()
#     serializer_class = IpAddressSerializers


class SingleIPView(RetrieveUpdateAPIView):
    queryset = IP_Address.objects.all()
    serializer_class = IpAddressSerializers


class DeleteIPView(RetrieveUpdateDestroyAPIView):
    queryset = IP_Address.objects.all()
    serializer_class = IpAddressSerializers

# Create your views here.
# class IPAddressViewSet(viewsets.ModelViewSet):
#     queryset = IP_Address.objects.all()
#     serializer_class = IpAddressSerializers


# class RouterView(APIView):

#     def get(self, request, format=None):
#         router_data = IP_Address.objects.all()
#         serializer = IpAddressSerializers(router_data, many=True)
#         response = {}
#         response["router_data"] = serializer.data
#         return JsonResponse(response, status=status.HTTP_200_OK, safe=False)

#     def post(self, request):
#         serializer = IpAddressSerializers(data=request.data)
#         response = {}
#         if serializer.is_valid():
#             serializer.save()
#             data = serializer.data
#             response["reason"] = data
#             response["success"] = True
#             return JsonResponse(response, status=status.HTTP_201_CREATED, safe=False)
#         else:
#             return JsonResponse(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST,
#                 safe=False
#             )


# class RouterDetail(APIView):

#     def get_router_object(self, pk):
#         try:
#             return IP_Address.objects.get(pk=pk)
#         except IP_Address.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_router_object(pk)
#         serializer = IpAddressSerializers(snippet)
#         return JsonResponse(serializer.data)

#     def put(self, request, pk, format=None):
#         router = self.get_router_object(pk)
#         serializer = IpAddressSerializers(router, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         router = self.get_router_object(pk)
#         router.delete()
#         return JsonResponse(status=status.HTTP_204_NO_CONTENT)
