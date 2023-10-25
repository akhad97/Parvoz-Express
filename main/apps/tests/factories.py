# import factory 
# from ..employee.models import Manager
# from faker import Faker

# fake = Faker()


# class ManagerFactory(factory.django.DjangoModelFactory):

#     class Meta:
#         model = Manager

#     full_name = fake.job()


import factory 
from ..flight.models.flight import Flight, FlightType
from ..hotel.models import Hotel
from ..outfit.models import Outfit, OutfitType
from ..employee.models import Manager, Guide
from ..transport.models import Transport
from faker import Faker
from pytest_factoryboy import register

from factory import Factory, Faker, SubFactory, Iterator
from datetime import datetime, timedelta

# fake = Faker()

class ManagerFactory(Factory):
    class Meta:
        model = Manager
    
    full_name = Faker('name')
    nickname = Faker('user_name')
    city = Faker('city')
    phone_number = Faker('phone_number')
    price = Faker('random_number', digits=5)
    is_active = True


class GuideFactory(Factory):
    class Meta:
        model = Guide
    
    full_name = Faker('name')
    nickname = Faker('user_name')
    city = Faker('city')
    phone_number = Faker('phone_number')
    price = Faker('random_number', digits=5)
    manager = SubFactory(ManagerFactory)
    is_active = True


class FlightTypeFactory(Factory):
    class Meta:
        model = FlightType
    
    title = Faker('random_element', elements=('Direct flight', 'Charter flight'))


class FlightFactory(Factory):
    class Meta:
        model = Flight
    
    flight_type = SubFactory(FlightTypeFactory)
    aviacompany_name_1 = Faker('company')
    # Add other fields as needed

class HotelFactory(Factory):
    class Meta:
        model = Hotel
    
    title = Faker('company')
    city = Faker('city')
    number_of_stars = Iterator([3, 4, 5])
    booking_duration = Faker('random_number', digits=2)
    # Add other fields as needed


class OutfitTypeFactory(Factory):
    class Meta:
        model = OutfitType
    
    title = Faker('random_element', elements=('Kamzul', 'Futbolka'))
    outfit_company = Faker('company')
    number_of_outfit = Faker('random_number', digits=2)
    price_for_one = Faker('random_number', digits=4)
    data = {}  # Add JSON data if needed
    is_active = True


class OutfitFactory(Factory):
    class Meta:
        model = Outfit
        
    outfit_type = SubFactory(OutfitTypeFactory)
    full_name = Faker('name')


class TransportFactory(Factory):
    class Meta:
        model = Transport
    
    transport_type = Faker('random_element', elements=('Bus', 'Taxi'))
    city = Faker('city')
    full_name = Faker('company_suffix')
    is_active = True




    


    

