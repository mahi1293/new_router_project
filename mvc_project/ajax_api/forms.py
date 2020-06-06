from django.http import JsonResponse
from django.views.generic import View
from django import forms
from django.forms.models import model_to_dict
from .models import IP_Address
from django.shortcuts import get_object_or_404
import logging
import json
from django.core.serializers.json import DjangoJSONEncoder
from netaddr import EUI, mac_bare
from macaddress import format_mac

logger = logging.getLogger(__name__)


class IPAddressForm(forms.ModelForm):
    class Meta:
        model = IP_Address
        fields = '__all__'


class IPAddressList(View):
    def get(self, request):
        ip_address = list(IP_Address.objects.all().values())
        data_list = []
        for ip in ip_address:
            ip_add_dict = {
                'ip_address': ip['ip_address'],
                'eth0': str(ip['eth0']),
                'host': ip['host'],
                'sap_id': str(ip['sap_id']),
                'id': ip['id']
            }
            data_list.append(ip_add_dict)

        data = {}
        data['ipaddress'] = data_list
        return JsonResponse(data)


class IPAddressDetail(View):
    def get(self, request, pk):
        ipaddress = get_object_or_404(IP_Address, pk=pk)
        ip_add_dict = {
                'ip_address': ipaddress.ip_address,
                'eth0': str(ipaddress.eth0),
                'host': ipaddress.host,
                'sap_id': str(ipaddress.sap_id),
                'id': ipaddress.id
            }
        data = {}
        data['ipaddress'] = ip_add_dict
        return JsonResponse(data)
