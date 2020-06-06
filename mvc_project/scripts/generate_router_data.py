import csv
import os

from django.conf import settings
from ajax_api.models import IP_Address

csv_path = os.path.join(settings.BASE_DIR, 'scripts/router_data.csv')


def create():
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        count = 0
        for row in reader:
            count += 1
            ipaddress, created = IP_Address.objects.get_or_create(ip_address=row['IP Address'])
            ipaddress.eth0 = row['Mac Address']
            ipaddress.host = row['Host Name']
            ipaddress.save()
            print("count: %s \r" % count, end=' ')
    return True
