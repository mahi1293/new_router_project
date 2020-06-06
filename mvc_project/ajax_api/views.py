from django.views.generic import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.http import JsonResponse
from .forms import IPAddressForm, IPAddressList, IPAddressDetail
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import IP_Address
from django.forms.models import model_to_dict
from django.forms.models import modelform_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, reverse


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


@method_decorator(csrf_exempt, name='dispatch')
class IPAdressCreate(AjaxableResponseMixin, CreateView):
    template_name = 'ip_address_form.html'
    form_class = IPAddressForm

    # def get_success_url(self):
    #     return reverse('book-detail', kwargs={'pk': self.object.pk})

#     model = IP_Address
#     fields = '__all__'

#     def post(self, request):
#         data = dict()
#         form = IPAddressForm(request.POST)
#         if form.is_valid():
#             room = form.save()
#             data['room'] = model_to_dict(room)
#         else:
#             data['error'] = "form not valid!"
#         return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class IPAddressUpdate(UpdateView):
    model = IP_Address
    fields = '__all__'
    template_name = 'ip_address_update_form.html'
    # def get(self, request, pk):
    #     ipaddress = get_object_or_404(IP_Address, pk=pk)
    #     ip_add_dict = {
    #             'ip_address': ipaddress.ip_address,
    #             'eth0': str(ipaddress.eth0),
    #             'host': ipaddress.host,
    #             'sap_id': str(ipaddress.sap_id),
    #             'id': ipaddress.id
    #         }
    #     data = {}
    #     data['ipaddress'] = ip_add_dict
    #     return JsonResponse(data)

    # def put(self, request, pk):
    # # create an object and redirect to detail page
    #     data = dict()
    #     room = IP_Address.objects.get(pk=pk)
    #     form = IPAddressForm(instance=room, data=request.POST)
    #     if form.is_valid():
    #         room = form.save()
    #         data['room'] = model_to_dict(room)
    #     else:
    #         data['error'] = "form not valid!"
    #     return JsonResponse(data)
    # def post(self, request, pk):
    #     data = dict()
    #     room = IP_Address.objects.get(pk=pk)
    #     form = IPAddressForm(instance=room, data=request.POST)
    #     if form.is_valid():
    #         room = form.save()
    #         data['room'] = model_to_dict(room)
    #     else:
    #         data['error'] = "form not valid!"
    #     return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class IPAddressDelete(View):
    def post(self, request, pk):
        data = dict()
        room = IP_Address.objects.get(pk=pk)
        if room:
            room.delete()
            data['message'] = "Room deleted!"
        else:
            data['message'] = "Error!"
        return JsonResponse(data)
