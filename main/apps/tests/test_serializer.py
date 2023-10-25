
# import pytest
# from rest_framework import status
# from main.apps.employee.models import Manager
# from main.apps.employee.serializers import ManagerSerializer
# from django.urls import reverse


# @pytest.fixture
# def manager_update_create_data_check_serializer(request):
#     # manager = manager_factory.create(full_name='Ali Aliev')
#     data = {
#         'complete-data': (
#             True, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': 'ali',
#                 'city': 'Tashkent',
#                 'phone_number': 1234567,
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'empty-nickname': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': '',
#                 'city': 'Tashkent',
#                 'phone_number': 1234567,
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'missing-nickname': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'city': 'Tashkent',
#                 'phone_number': 1234567,
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'missing-full_name': (
#             False, {
#                 'nickname': 'alik',
#                 'city': 'Tashkent',
#                 'phone_number': 1234567,
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'empty-full_name': (
#             False, {
#                 'full_name': '',
#                 'nickname': 'ali',
#                 'city': 'Tashkent',
#                 'phone_number': 1234567,
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'invalid-price-format': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': 'ali',
#                 'city': 'Tashkent',
#                 'phone_number': 1234567,
#                 'price': 'price',
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'missing-price': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': 'ali',
#                 'city': 'Tashkent',
#                 'phone_number': 1234567,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'empty-price': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': 'ali',
#                 'city': 'Tashkent',
#                 'price': '',
#                 'phone_number': 1234567,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'missing-city': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': 'ali',
#                 'phone_number': 1234567,
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'empty-city': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': 'ali',
#                 'city': '',
#                 'phone_number': 1234567,
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'missing-phone_number': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': 'ali',
#                 'city': 'Tashkent',
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#         'empty-phone_number': (
#             False, {
#                 'full_name': 'Ali Aliev',
#                 'nickname': 'ali',
#                 'city': 'Tashkent',
#                 'phone_number': '',
#                 'price': 5000,
#                 'password': 'test-pass',
#                 'is_acitve': True
#             }
#         ),
#     }
#     return data[request.param]

# @pytest.mark.django_db
# @pytest.mark.parametrize('manager_update_create_data_check_serializer',[
#     'complete-data', 
#     'missing-full_name', 
#     'empty-full_name', 
#     'invalid-price-format',
#     'empty-phone_number',
#     'missing-phone_number',
#     'empty-city',
#     'missing-city',
#     'missing-price',
#     'empty-price',
#     'empty-nickname',
#     'missing-nickname'
#     ], 
#                           indirect=True)
# def test_manager_serializer(manager_update_create_data_check_serializer: tuple):
#     validity, data = manager_update_create_data_check_serializer
#     serializer = ManagerSerializer(data=data)
#     assert serializer.is_valid() == validity
#     if serializer.is_valid():
#         serializer.save()
#         expected = ['id', 'guid', 'full_name', 'nickname', 'city', 'phone_number', 'price', 'password', 'is_active']
#         returnned = dict(serializer.data).keys()
#         print(sorted(expected))
#         print(sorted(returnned))
        
 


import pytest
from rest_framework import status
from main.apps.package.serializer import TourPackageSerializer
from django.urls import reverse


@pytest.fixture
def package_data_check_serializer(
    request, flight_factory, hotel_factory,
    outfit_factory, transport_factory, manager_factory, guide_factory
    ):
    flight = flight_factory.create()
    hotel = hotel_factory.create()
    outfit = outfit_factory.create()
    transport = transport_factory.create()
    manager = manager_factory.create()
    guide = guide_factory.create()

    print('flight', flight)
    print('hotel', hotel)
    print('outfit', outfit)
    print('transport', transport)
    print('manager', manager)
    print('guide', guide)
    data = {
        'complete-data': (
            True, {
                'title': 'Tourpackage',
                'start_date': '2021-01-01 00:00:00+00:00',
                'end_date': '2021-01-01 00:00:00+00:00',
                'additional_expense': 3000.00,
                'number_of_seats': 150,
                'price_for_person': 1200.00,
                'flight':flight.id,
                'hotel': [hotel.id],
                'outfit':[outfit.id],
                'transport': [transport.id],
                'manager':manager.id,
                'guide':[guide.id],
                'date_data':{'key':'test'},
                'hotel_date':{'key':'test'},
                'outfit_data':{'key':'test'},
                'currency': 12150.00,
                'status': 'CREATED',
                'is_active':True,
                'transport_full_names':['transport']
            }
        ),
    }
    return data[request.param]


@pytest.mark.django_db
@pytest.mark.parametrize('package_data_check_serializer',[
    'complete-data'
    ], 
                          indirect=True)
def test_package_serializer(package_data_check_serializer: tuple):
    validity, data = package_data_check_serializer
    serializer = TourPackageSerializer(data=data)
    print(validity)
    print(serializer.is_valid())
    assert serializer.is_valid() == validity