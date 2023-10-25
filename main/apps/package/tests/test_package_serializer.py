
# import pytest
# from rest_framework import status
# from main.apps.package.serializer import TourPackageSerializer
# from django.urls import reverse


# @pytest.fixture
# def package_data_check_serializer(
#     request, flight_factory, hotel_factory,
#     outfit_factory, transport_factory, manager_factory, guide_factory
#     ):
#     flight = flight_factory.create(aviacompany_name_1='Name')
#     hotel = hotel_factory.create(title='title')
#     outfit = outfit_factory.create(outfit_company='company')
#     transport = transport_factory.create(title='title')
#     manager = manager_factory.create(full_name='name')
#     guide = guide_factory.create(full_name='name')
#     data = {
#         'complete-data': (
#             True, {
#                 'title': 'Tourpackage',
#                 'start_date': '2021-01-01 00:00:00+00:00',
#                 'end_date': '2021-01-01 00:00:00+00:00',
#                 'additional_expense': 3000.00,
#                 'number_of_seats': 150,
#                 'price_for_person': 1200.00,
#                 'flight':flight.id,
#                 'hotel': [hotel.id],
#                 'outfit':[outfit.id],
#                 'transport': [transport.id],
#                 'manager':manager.id,
#                 'guide':[guide.id],
#                 'date_data':{'key':'test'},
#                 'hotel_date':{'key':'test'},
#                 'outfit_data':{'key':'test'},
#                 'currency': 12150.00,
#                 'status': 'CREATED',
#                 'is_active':True,
#                 'transport_full_names':['transport']
#             }
#         ),
#     }
#     return data[request.param]


# @pytest.mark.django_db
# @pytest.mark.parametrize('package_data_check_serializer',[
#     'complete-data'
#     ], 
#                           indirect=True)
# def test_package_serializer(package_data_check_serializer: tuple):
#     validity, data = package_data_check_serializer
#     serializer = TourPackageSerializer(data=data)
#     assert serializer.is_valid() == validity
#     # if serializer.is_valid():
#     #     serializer.save()
#     #     expected = [
#     #         'id', 
#     #         'guid', 
#     #         'full_name', 
#     #         'nickname', 
#     #         'city', 
#     #         'phone_number', 
#     #         'price', 
#     #         'password', 
#     #         'is_active'
#     #         ]
#     #     returnned = dict(serializer.data).keys()
#     #     print(sorted(expected))
#     #     print(sorted(returnned))
        
 
