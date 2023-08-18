from rest_framework import generics 
from rest_framework.response import Response
from ...flight.models.flight import (
    Flight, 
    FlightType,
    FlightBook
)
from ...flight.serializer.flight import (
    FlightSerializer, 
    FlightCreateSerializer, 
    FlightTypeSerializer,
    FlightBookCreateSerializer,
    FlightBookListSerializer,
    FlightBookUpdateSerializer
)
from ...common.views import CustomListView



class FlightLandingSeachAPIView(CustomListView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_queryset(self):
        params = self.request.query_params
        flight_type = params.get('flight_type', None)
        place_of_departure = params.get('place_of_departure', None)
        place_of_arrival_1 = params.get('place_of_arrival_1', None)
        place_of_arrival_2 = params.get('place_of_arrival_2', None)
        departure_time = params.get('departure_time', None)
        qs = Flight.objects.all()

        if flight_type:
            qs = qs.filter(flight_type__title__icontains=flight_type)
        
        if place_of_departure:
            qs = qs.filter(place_of_departure_1__icontains=place_of_departure)
        
        if place_of_arrival_1:
            qs = qs.filter(place_of_arrival_1__icontains=place_of_arrival_1)
        
        if place_of_arrival_2:
            qs = qs.filter(place_of_arrival_2__icontains=place_of_arrival_2)

        if departure_time:
            qs = qs.filter(departure_time_1__icontains=departure_time)       
        return qs

flight_landing_serach_api_view = FlightLandingSeachAPIView.as_view()



class FlightTypeListAPIView(CustomListView):
    queryset = FlightType.objects.all()
    serializer_class = FlightTypeSerializer


flight_type_list_api_view = FlightTypeListAPIView.as_view()


class FlightListAPIView(CustomListView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'guid'
    search_fields = ['aviacompany_name_1', 'place_of_departure_1']

    def get_queryset(self):
        queryset = super().get_queryset()
        flight_type = self.request.query_params.get('flight_type', None)
        if flight_type:
            queryset = queryset.filter(flight_type__guid=flight_type)
        return queryset


flight_list_api_view = FlightListAPIView.as_view()


class FlightCreateAPIView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightCreateSerializer

flight_create_api_view = FlightCreateAPIView.as_view()


class FlightDetailAPIView(generics.RetrieveAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'guid'

flight_detail_list_api_view = FlightDetailAPIView.as_view()


class FlightDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    lookup_field = 'guid'

flight_update_list_api_view = FlightDetailAPIView.as_view()


class FlightBookCreateAPIView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightBookCreateSerializer

flight_book_create_api_view = FlightBookCreateAPIView.as_view()


class FlightBookListAPIView(CustomListView):
    queryset = FlightBook.objects.all()
    serializer_class = FlightBookListSerializer

flight_book_list_api_view = FlightBookListAPIView.as_view()


class FLightBookUpdateAPIView(generics.UpdateAPIView):
    queryset = FlightBook.objects.all()
    serializer_class = FlightBookUpdateSerializer
    lookup_field = 'guid'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Successfully updated'})
        return Response({'message': 'failed', 'details': serializer.errors})

flight_book_update_api_view = FLightBookUpdateAPIView.as_view()