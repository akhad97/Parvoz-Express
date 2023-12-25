from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import (
    Guide, 
    Manager,
    ManagerCalculation,
    GuideCalculation
)
from .serializers import (
    ManagerCreateSerializer,
    ManagerUpdateSerializer, 
    GuideSerializer,
    ManagerCalculationListSerializer,
    ManagerCalculationCreateSerializer,
    GuideCalculationListSerializer,
    GuideCalculationCreateSerializer,
    GuideLoginSerializer,
    ManagerLoginSerializer
)
from ..common.views import CustomListView
from ..common.utils import (
    get_prepayment_percentage, 
    get_remained_amount_percentage, 
    get_unpaid_percentage
)
from django.contrib.auth.hashers import check_password


class GuideLoginAPIView(generics.GenericAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = GuideLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            try:
                guide = Guide.objects.get(phone_number=phone_number)
            except Guide.DoesNotExist:
                return Response({'message':'Guide not found!'}, status=status.HTTP_404_NOT_FOUND)
            response_data = {
                'data': serializer.data,
                'guid':guide.guid
            }
            if check_password(password, guide.password):
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid phone number or password', 'status':status.HTTP_401_UNAUTHORIZED})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

guide_login_api_view = GuideLoginAPIView.as_view()


class ManagerLoginAPIView(generics.GenericAPIView):
    queryset = Manager.objects.filter(is_active=True)
    serializer_class = ManagerLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = ManagerLoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            try:
                manager = Manager.objects.get(phone_number=phone_number)
            except Manager.DoesNotExist:
                return Response({'message':'Manager not found!'}, status=status.HTTP_404_NOT_FOUND)
            response_data = {
                'data': serializer.data,
                'guid':manager.guid
            }
            if check_password(password, manager.password):
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid phone number or password', 'status':status.HTTP_401_UNAUTHORIZED})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

manager_login_api_view = ManagerLoginAPIView.as_view()


class ManagerListAPIView(CustomListView):
    queryset = Manager.objects.all()
    serializer_class = ManagerUpdateSerializer

    def get_queryset(self):
        params = self.request.query_params
        query = params.get('query')
        qs = Manager.objects.all()
        if query:
            qs = qs.filter(
                Q(full_name__icontains=query) |
                Q(nickname__icontains=query) |
                Q(city__icontains=query)
            ).distinct()
        return qs
    

manager_list_api_view = ManagerListAPIView.as_view()


class ManagerDetailAPIView(generics.RetrieveAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerUpdateSerializer
    lookup_field = 'guid'

manager_detail_api_view = ManagerDetailAPIView.as_view()


class ManagerDestroyAPIView(generics.DestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerUpdateSerializer
    lookup_field = 'guid'

manager_delete_api_view = ManagerDestroyAPIView.as_view()


class ManagerUpdateAPIView(generics.UpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerUpdateSerializer
    lookup_field = 'guid'

manager_update_api_view = ManagerUpdateAPIView.as_view()


class ManagerCreateAPIView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerCreateSerializer

manager_create_api_view = ManagerCreateAPIView.as_view()


class GuideListAPIView(CustomListView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def get_queryset(self): 
        params = self.request.query_params
        query = params.get('query')
        qs = Guide.objects.all()
        if query:
            qs = qs.filter(
                Q(full_name__icontains=query) |
                Q(nickname__icontains=query) |
                Q(city__icontains=query)
                ).distinct()
        return qs

guide_list_api_view = GuideListAPIView.as_view()


class ManagerGuideListAPIView(CustomListView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    def get_queryset(self):
        guides = Guide.objects.filter(manager__id=self.kwargs['pk'])
        return guides

manager_guide_list_api_view = ManagerGuideListAPIView.as_view()


class GuideDetailAPIView(generics.RetrieveAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    lookup_field = 'guid'

guide_detail_api_view = GuideDetailAPIView.as_view()


class GuideDeleteAPIView(generics.DestroyAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    lookup_field = 'guid'

guide_delete_api_view = GuideDeleteAPIView.as_view()


class GuideUpdateAPIView(generics.UpdateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    lookup_field = 'guid'

guide_update_api_view = GuideUpdateAPIView.as_view()


class GuideCreateAPIView(generics.CreateAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

guide_create_api_view = GuideCreateAPIView.as_view()


class ManagerCalculationListAPIView(CustomListView):
    queryset = ManagerCalculation.objects.all()
    serializer_class = ManagerCalculationListSerializer

managercalculation_list_api_view = ManagerCalculationListAPIView.as_view()


class ManagerCalculationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ManagerCalculation.objects.all()
    serializer_class = ManagerCalculationListSerializer

managercalculation_detail_api_view = ManagerCalculationDetailAPIView.as_view()


class ManagerCalculationCreateAPIView(generics.CreateAPIView):
    queryset = ManagerCalculation.objects.all()
    serializer_class = ManagerCalculationCreateSerializer

managercalculation_create_api_view = ManagerCalculationCreateAPIView.as_view()

class ManagerCalculationUpdateAPIView(generics.UpdateAPIView):
    queryset = ManagerCalculation.objects.all()
    serializer_class = ManagerCalculationListSerializer

managercalculation_update_api_view = ManagerCalculationUpdateAPIView.as_view()


class GuideCalculationListAPIView(CustomListView):
    queryset = GuideCalculation.objects.all()
    serializer_class = GuideCalculationListSerializer

guidecalculation_list_api_view = GuideCalculationListAPIView.as_view()


class GuideCalculationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GuideCalculation.objects.all()
    serializer_class = GuideCalculationListSerializer

guidecalculation_detail_api_view = GuideCalculationDetailAPIView.as_view()


class GuideCalculationUpdateAPIView(generics.UpdateAPIView):
    queryset = GuideCalculation.objects.all()
    serializer_class = GuideCalculationListSerializer

guidecalculation_update_api_view = GuideCalculationUpdateAPIView.as_view()


class GuideCalculationCreateAPIView(generics.CreateAPIView):
    queryset = GuideCalculation.objects.all()
    serializer_class = GuideCalculationCreateSerializer

guidecalculation_create_api_view = GuideCalculationCreateAPIView.as_view()



@api_view(['GET'])
def managercalculation_analytics(request):
    model = ManagerCalculation
    prepayment_percentage = get_prepayment_percentage(model)
    remained_amount_percentage = get_remained_amount_percentage(model)
    unpaid_percentage = get_unpaid_percentage(model)

    last_manager = model.objects.select_related('manager').last()

    data = {
        'manager': last_manager.manager.full_name if last_manager else None,
        **prepayment_percentage,
        **remained_amount_percentage,
        'unpaid_percentage': unpaid_percentage,
    }
    return Response(data)
 
managercalculation_data_api_view = managercalculation_analytics


@api_view(['GET'])
def guidecalculation_analytics(request):
    model = GuideCalculation
    prepayment_percentage = get_prepayment_percentage(model)
    remained_amount_percentage = get_remained_amount_percentage(model)
    unpaid_percentage = get_unpaid_percentage(model)

    last_guide = model.objects.select_related('guide').last()

    data = {
        'guide': last_guide.guide.full_name if last_guide else None,
        **prepayment_percentage,
        **remained_amount_percentage,
        'unpaid_percentage': unpaid_percentage,
    }
    return Response(data)
 
guidecalculation_data_api_view = guidecalculation_analytics

