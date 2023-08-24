from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from .models import Outfit, OutfitType, OutfitCalculation
from .serializers import (
    OutfitTypeListSerializer,
    OutfitTypeCreateSerializer,
    OutfitListSerializer,
    OutfitCreateSerializer,
    OutfitCalculationCreateSerializer,
    OutfitUpdateSerializer
)
from ..common.utils import (
    get_prepayment_percentage, 
    get_remained_amount_percentage, 
    get_unpaid_percentage
)
from ..common.views import CustomListView, CustomCreateAPIView, CustomDetailView
from ..common.validations import CustomValidationError


class OutfitListAPIView(CustomListView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitListSerializer


    def get_queryset(self):
        params = self.request.query_params
        query = params.get('query', None)

        types = OutfitType.objects.all()    
        qs = Outfit.objects.filter(outfit_type__in=types)
        if query:
            qs = qs.filter(
                Q(full_name__icontains=query) |
                Q(outfit_type__outfit_company__icontains=query) |
                Q(outfit_type__title__icontains=query)
            )
        
        return qs
    
outfit_list_api_view = OutfitListAPIView.as_view()


class OutfitCreateAPIView(CustomCreateAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        outfit_type = data['outfit_type']
        outfit_types = []
        for i in outfit_type:
            type = OutfitType.objects.create(**i)
            outfit_types.append(type)

        outfits = []
        for outfit_type in outfit_types:
            outfit = Outfit.objects.create(outfit_type=outfit_type, full_name=data['full_name'])
            outfits.append(outfit)

        return self.success_response(outfits)
    

outfit_create_api_view = OutfitCreateAPIView.as_view()


class OutfitDetailAPIView(CustomDetailView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitUpdateSerializer

    def get_object(self, pk):
        try:
            return Outfit.objects.get(pk=pk)
        except Outfit.DoesNotExist:
            raise CustomValidationError(msg='Not Found')
    
    def get(self, request, pk):
        outfit = self.get_object(pk)
        serializer = OutfitUpdateSerializer(outfit)
        return self.success_response(results=serializer.data)

    def update(self, request, pk):
        data = request.data
        outfit = self.get_object(pk)
        outfit_type_data = data.get('outfit_type')
        
        if outfit_type_data:
            outfit_type = OutfitType.objects.get(id=outfit_type_data['id'])
            outfit.outfit_type = outfit_type

        serializer = self.serializer_class(outfit, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return self.success_response(results=serializer.data)
    
    
    def delete(self, request, pk):
        outfit = Outfit.objects.get(id=pk)
        outfit.delete()
        return Response({'message': 'Outfit successfully deleted!'})

outfit_detail_api_view = OutfitDetailAPIView.as_view()


class OutfitTypeListAPIView(CustomListView):
    queryset = OutfitType.objects.all()
    serializer_class = OutfitTypeListSerializer

outfittype_list_api_view = OutfitTypeListAPIView.as_view()


class OutfitTypeCreateAPIView(CustomCreateAPIView):
    queryset = OutfitType.objects.all()
    serializer_class = OutfitTypeCreateSerializer

outfittype_create_api_view = OutfitTypeCreateAPIView.as_view()


class OutfitCalculationListAPIView(CustomListView):
    queryset = OutfitCalculation.objects.all()
    serializer_class = OutfitCalculationCreateSerializer


outfit_calculation_list_api_view = OutfitCalculationListAPIView.as_view()

class OutfitCalculationCreateAPIView(CustomCreateAPIView):
    queryset = OutfitCalculation.objects.all()
    serializer_class = OutfitCalculationCreateSerializer


outfit_calculation_create_api_view = OutfitCalculationCreateAPIView.as_view()

    
class SingleOutfitCalculationDetailAPIView(CustomListView):
    queryset = OutfitCalculation.objects.all()
    serializer_class = OutfitCalculationCreateSerializer

    def get_queryset(self):
        params = self.request.query_params
        qs = OutfitCalculation.objects.filter(outfit=self.kwargs['pk'])
                
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)
        total_amount = params.get('total_amount', None)
        prepayment = params.get('prepayment', None)
        remained_amount = params.get('remained_amount', None)

        if from_date and to_date:
            try:
                from_date = datetime.strptime(params.get('from_date', None), '%Y-%m-%d')
                from_date = timezone.make_aware(from_date, timezone.get_current_timezone())
                to_date = params.get('to_date', None) + ' 23:59:59'
                to_date = datetime.strptime(to_date, '%Y-%m-%d %H:%M:%S')
                to_date = timezone.make_aware(to_date, timezone.get_current_timezone())
                qs = qs.filter(Q(from_date__range=[from_date, to_date]) | Q(to_date__range=[from_date, to_date]))
            except Exception as e:
                raise CustomValidationError(msg=e.args)
            
        if total_amount:
            qs = qs.filter(Q(total_amount__icontains=total_amount))
        
        if prepayment:
            qs = qs.filter(Q(prepayment__icontains=prepayment))
        
        if remained_amount:
            qs = qs.filter(Q(remained_amount__icontains=remained_amount))
        return qs


single_outfit_calculation_detail_api_view = SingleOutfitCalculationDetailAPIView.as_view()



@api_view(['GET'])
def outfitcalculation_analytics(request):
    model = OutfitCalculation
    prepayment_percentage = get_prepayment_percentage(model)
    remained_amount_percentage = get_remained_amount_percentage(model)
    unpaid_percentage = get_unpaid_percentage(model)

    last_outfit = OutfitCalculation.objects.select_related('outfit').last()
    

    data = {
        'outfit': last_outfit.outfit.id if last_outfit else None,
        'prepayment_percentage': prepayment_percentage,
        'remained_amount_percentage': remained_amount_percentage,
        'unpaid_percentage': unpaid_percentage,
    }
    return Response(data)

 
outfitcalculation_data_api_view = outfitcalculation_analytics