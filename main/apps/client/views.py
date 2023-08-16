from rest_framework import generics
from rest_framework.response import Response
from .models import (
    Client, 
    Partner,
    VisaClient
)
from .serializers import (
    ClientSerializer, 
    ClientCreateSerializer,
    PartnerSerializer, 
    PartnerCreateSerializer,
    VisaClientSerializer
)
from ..common.views import CustomListView


class ClientListAPIView(CustomListView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'guid'

    def get_queryset(self):
        guid = self.kwargs['guid']
        clients = Client.objects.filter(tour_package__guid=guid)
        return clients
    
client_list_api_view = ClientListAPIView.as_view()


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer

client_create_api_view = ClientCreateAPIView.as_view()


class ClientDetailAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'guid'
    
client_detail_api_view = ClientDetailAPIView.as_view()


class ClientUpdateAPIView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'guid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'visa file updated succesfully'})
        return Response({'message': 'failed', 'details': serializer.errors})

    
client_update_api_view = ClientUpdateAPIView.as_view()


class PartnerListAPIView(CustomListView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    lookup_field = 'guid'

    def get_queryset(self):
        guid = self.kwargs['guid']
        partners = Partner.objects.filter(client__guid=guid)
        return partners

partner_list_api_view = PartnerListAPIView.as_view()



class PartnerCreateAPIView(generics.CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerCreateSerializer

partner_create_api_view = PartnerCreateAPIView.as_view()


class PartnerUpdateAPIView(generics.UpdateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    lookup_field = 'guid'

    
partner_update_api_view = PartnerUpdateAPIView.as_view()


class VisaClientListAPIView(CustomListView):
    queryset = VisaClient.objects.all()
    serializer_class = VisaClientSerializer

    def get_queryset(self):
        partners = VisaClient.objects.filter(visa__id=self.kwargs['pk'])
        return partners

visa_client_list_api_view = VisaClientListAPIView.as_view()


class VisaClientCreateAPIView(generics.CreateAPIView):
    queryset = VisaClient.objects.all()
    serializer_class = VisaClientSerializer

visa_client_create_api_view = VisaClientCreateAPIView.as_view()


class VisaClientUpdateAPIView(generics.UpdateAPIView):
    queryset = VisaClient.objects.all()
    serializer_class = VisaClientSerializer
    lookup_field = 'guid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'visa file updated succesfully'})
        return Response({'message': 'failed', 'details': serializer.errors})

visa_client_update_api_view = VisaClientUpdateAPIView.as_view()

