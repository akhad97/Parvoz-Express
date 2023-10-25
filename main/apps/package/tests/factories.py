import factory 
from ...flight.models.flight import Flight
from ...hotel.models import Hotel
from ...outfit.models import Outfit
from ...employee.models import Manager, Guide
from ...transport.models import Transport
from faker import Faker
from pytest_factoryboy import register

fake = Faker()


class FlightFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Flight

    aviacompany_name_1 = fake.job()


class HotelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hotel
    
    title = fake.job()


class OutfitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Outfit
    
    outfit_company = fake.job()


class ManagerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Manager
    
    full_name = fake.job()


class GuideFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Guide
    
    full_name = fake.job()


class TransportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transport
    
    city = fake.job()

    
register(ManagerFactory)
register(TransportFactory)
register(HotelFactory)
register(FlightFactory)
register(OutfitFactory)




    

