from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.urls import reverse

from macaddress.fields import MACAddressField


class IP_Address(models.Model):
    ip_address = models.GenericIPAddressField()
    eth0 = MACAddressField(null=True, blank=True)
    host = models.CharField(max_length=200, unique=True)
    sap_id = models.UUIDField(
        # primary_key=True,
        default=uuid.uuid4,
        editable=False)

    def __str__(self):
        return self.host

    def get_absolute_url(self):
        return reverse('ipaddress_main')
