from django.urls import path, include
from django.views.generic.base import TemplateView
from ajax_api import views, forms
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('ipaddress/', TemplateView.as_view(template_name="main.html"), name='ipaddress_main'),
    path('ipaddress/list', forms.IPAddressList.as_view(), name='ipaddress_list'),
    path('ipaddress/create', views.IPAdressCreate.as_view(), name='ipaddress_create'),
    path('ipaddress/update/<int:pk>', views.IPAddressUpdate.as_view(), name='ipaddress_update'),
    path('ipaddress/delete/<int:pk>', views.IPAddressDelete.as_view(), name='ipaddress_delete'),
    path('ipaddress/<int:pk>', forms.IPAddressDetail.as_view(), name='ipaddress_detail')
]