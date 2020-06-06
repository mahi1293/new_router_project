from django.urls import path, include
from router_rest_api import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('ipaddress', views.IPAddressViewSet)


urlpatterns = [
    # path("ipaddresses/", views.RouterView.as_view(), name='api_view'),
    # path("ipaddresses/<int:pk>/", views.RouterDetail.as_view(), name='api_detail'),
    # path('', include(router.urls)),
    path('ips/<int:pk>', views.SingleIPView.as_view()),
    path('ips/', views.IPAddressView.as_view()),
    path('ips/create/', views.IPViewSet.as_view()),
    path('ips/delete/<int:pk>', views.DeleteIPView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
