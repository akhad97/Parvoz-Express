from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
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
        params = self.request.query_params
        clients = Client.objects.filter(tour_package__guid=guid).select_related('tour_package', 'hotel', 'visa')
        full_name = params.get('search', None)
        if full_name:
            clients = clients.filter(Q(full_name__icontains=full_name))
        return clients
    
    
client_list_api_view = ClientListAPIView.as_view()



class ClientCreateAPIView(APIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permissions = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serialzier = ClientCreateSerializer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, 
                            status=status.HTTP_201_CREATED)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

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


class ClientDeleteAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'guid'

    def delete(self, request, *args, **kwargs):
        guid = self.kwargs['guid']
        instance = Client.objects.get(guid=guid)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
client_delete_api_view = ClientDeleteAPIView.as_view()


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


class VisaClientDeleteAPIView(generics.DestroyAPIView):
    queryset = VisaClient.objects.all()
    serializer_class = VisaClientSerializer
    lookup_field = 'guid'

    def delete(self, request, *args, **kwargs):
        guid = self.kwargs['guid']
        instance = VisaClient.objects.get(guid=guid)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
visa_client_delete_api_view = VisaClientDeleteAPIView.as_view()