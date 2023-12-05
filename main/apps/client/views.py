import pdfkit
import json
import requests
from django.template.loader import render_to_string
from django.http import HttpResponse
from datetime import datetime
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
from django.core.files.base import ContentFile



class ClientListAPIView(CustomListView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'guid'

    def get_queryset(self):
        guid = self.kwargs['guid']
        params = self.request.query_params
        clients = Client.objects.filter(tour_package__guid=guid).select_related('tour_package', 'hotel', 'visa')
        full_name = params.get('search', None)
        created_by = params.get('created_by', None)
        if full_name:
            clients = clients.filter(Q(full_name__icontains=full_name))
        if created_by=='NMA1':
            clients = clients.filter(created_by='NMA1')
        if created_by=='NMA2':
            clients = clients.filter(created_by='NMA2')
        if created_by=='NMA3':
            clients = clients.filter(created_by='NMA3')
        if created_by=='NMA4':
            clients = clients.filter(created_by='NMA4')
        if created_by=='QQN':
            clients = clients.filter(created_by='QQN/0001')
        if created_by=='MRN':
            clients = clients.filter(created_by='MRN')
        if created_by=='TAS':
            clients = clients.filter(created_by='TAS')
        if created_by=='SKD':
            clients = clients.filter(created_by='SKD')
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
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'visa file updated succesfully'})
        return Response({'message': 'failed', 'details': serializer.errors})
    
    
    def patch(self, request, *args, **kwargs):
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



class ClientPDFView(APIView):
    # agent_id=""
    # image=None
    # select=""
    # select_1=""
    # select_2=""
    # select_3=""
    # select_4=""
    # select_5=""
    # select_6=""
    # select_7=""
    # select_8=""
    def post(self, request, *args, **kwargs):
        global image, agent_id, select, select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, number, price_for_number, price_for_text, address
        image = request.data.get('image')
        agent_id = request.query_params.get('agent_id')
        select = request.data.get('select')
        select_1 = request.data.get('select_1')
        select_2 = request.data.get('select_2')
        select_3 = request.data.get('select_3')
        select_4 = request.data.get('select_4')
        select_5 = request.data.get('select_5')
        select_6 = request.data.get('select_6')
        select_7 = request.data.get('select_7')
        select_8 = request.data.get('select_8')
        number = request.data.get('number')
        price_for_number = request.data.get('price_for_number')
        price_for_text = request.data.get('price_for_text')
        address = request.data.get('address')
        guid = kwargs.get('guid', None)
        if guid is not None:
            get_request_url = f'https://5d63-84-54-74-20.ngrok-free.app/api/v1/client/client-pdf/{guid}'
            # get_request_params = {'param1': 'value1', 'param2': 'value2'}
            get_response = requests.get(get_request_url)
            get_response_data = get_response.json() if get_response.status_code == 200 else None
            return Response({'message': 'Image saved successfully', 'get_response_data': get_response_data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Client ID (pk) not provided'}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, guid, *args, **kwargs):
        client = Client.objects.get(guid=guid)
        serializer = ClientSerializer(client)
        client_first_name = client.first_name
        client_last_name = client.last_name
        client_middle_name = client.middle_name
        client_passport_series = client.passport_series

        tourpackage_start_year = client.tour_package.start_date.year
        tourpackage_start_month = client.tour_package.start_date.strftime('%B')
        tourpackage_start_day = client.tour_package.start_date.day
        tourpackage_end_year = client.tour_package.end_date.year
        tourpackage_end_month = client.tour_package.end_date.strftime('%B')
        tourpackage_end_day = client.tour_package.end_date.day

        year =  datetime.now().year
        month =  datetime.now().strftime('%B')
        day =  datetime.now().day
        hotel_name = client.hotel.title
        html_content = render_to_string('client.html', 
                                        {
                                            'data': serializer.data, 
                                            'client_first_name': client_first_name,
                                            'client_last_name': client_last_name,
                                            'client_middle_name': client_middle_name,
                                            'client_passport_series': client_passport_series,
                                            'year': year,
                                            'month': month,
                                            'day': day,
                                            'hotel_name': hotel_name,
                                            'tourpackage_start_year': tourpackage_start_year,
                                            'tourpackage_start_month': tourpackage_start_month,
                                            'tourpackage_start_day': tourpackage_start_day,
                                            'tourpackage_end_year': tourpackage_end_year,
                                            'tourpackage_end_month': tourpackage_end_month,
                                            'tourpackage_end_day': tourpackage_end_day,
                                            'agent_id': agent_id,
                                            'image': image,
                                            'select': select,
                                            'select_1': select_1,
                                            'select_2': select_2,
                                            'select_3': select_3,
                                            'select_4': select_4,
                                            'select_5': select_5,
                                            'select_6': select_6,
                                            'select_7': select_7,
                                            'select_8': select_8,
                                            'number': number,
                                            'price_for_number': price_for_number,
                                            'price_for_text': price_for_text,
                                            'address': address
                                        })
        pdf_file = pdfkit.from_string(html_content, False) 
        response = HttpResponse(pdf_file, content_type='application/pdf') 
        filename = f'{client.first_name}_{client.last_name}_{year}_{month}_{day}.pdf'
        client.contract_file.save(f'{client.first_name}_{client.last_name}_{year}_{month}_{day}.pdf', ContentFile(pdf_file))
        contract_file_url = client.contract_file.url
        response_content = {
            'contract_file_url': contract_file_url,
            'message': 'PDF generated successfully'
        }
        response = HttpResponse(json.dumps(response_content), content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response


client_pdf_api_view = ClientPDFView.as_view()