from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import OtherExpense
from .serializers import (
    OtherExpenseListSerializer,
    OtherExpenseCreateSerializer,
    TourpackageOtherExpenseCreateSerializer
)
from ..common.views import CustomListView, CustomDetailView, CustomCreateAPIView
from .models import calculate_category_percentages


class TourpakcageOtherExpenseCreateAPIView(CustomCreateAPIView):
    queryset = OtherExpense.objects.all()
    serializer_class = TourpackageOtherExpenseCreateSerializer

tourpackage_otherexpense_create_api_view = TourpakcageOtherExpenseCreateAPIView.as_view()


class OtherExpenseListAPIView(CustomListView):
    queryset = OtherExpense.objects.all()
    serializer_class = OtherExpenseListSerializer

    def get_queryset(self):
        # user = self.request.user
        params = self.request.query_params
        query = params.get('query', None)

        expenses = OtherExpense.objects.all() # need to filter based on user or smth 

        if query:
            expenses = expenses.filter(Q(title__icontains=query) | Q(amount__icontains=query))

        return expenses

otherexpense_list_api_view = OtherExpenseListAPIView.as_view()


class OtherExpenseCreateAPIView(CustomCreateAPIView):
    queryset = OtherExpense.objects.all()
    serializer_class = OtherExpenseCreateSerializer

otherexpense_create_api_view = OtherExpenseCreateAPIView.as_view()


class OtherExpenseDetailAPIView(CustomDetailView):
    queryset = OtherExpense.objects.all()
    serializer_class = OtherExpenseListSerializer
    lookup_field = 'guid'

otherexpense_update_api_view = OtherExpenseDetailAPIView.as_view()


@api_view(['GET'])
def otherexpense_view(request):
    category_percentages = calculate_category_percentages()
    return Response({'category_percentages': category_percentages})


otherexpense_view_data_api_view = otherexpense_view

