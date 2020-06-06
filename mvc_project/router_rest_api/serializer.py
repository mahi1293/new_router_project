from rest_framework import serializers
from ajax_api.models import IP_Address


class IpAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = IP_Address
        fields = "__all__"
