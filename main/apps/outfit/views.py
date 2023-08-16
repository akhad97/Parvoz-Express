from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q


from .models import Outfit, OutfitType, OutfitCalculation
from .serializers import (
    OutfitTypeListSerializer,
    OutfitTypeCreateSerializer,
    OutfitListSerializer,
    OutfitCreateSerializer,
    OutfitCalculationCreateSerializer,
    OutfitUpdateSerializer
)

from ..common.utils import get_prepayment_percentage, get_remained_amount_percentage, get_unpaid_percentage
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
        return OutfitCalculation.objects.filter(outfit=self.kwargs['pk'])


single_outfit_calculation_detail_api_view = SingleOutfitCalculationDetailAPIView.as_view()


@api_view(['GET'])
def outfitcalculation_analytics(request):
    model = OutfitCalculation
    prepayment_percentage = get_prepayment_percentage(model)
    remained_amount_percentage = get_remained_amount_percentage(model)
    unpaid_percentage = get_unpaid_percentage(model)

    data = {
        'outfit': OutfitCalculation.objects.last().outfit.id,
        'prepayment_percentage': prepayment_percentage,
        'remained_amount_percentage': remained_amount_percentage,
        'unpaid_percentage': unpaid_percentage,
    }
    return Response(data)

 
outfitcalculation_data_api_view = outfitcalculation_analytics