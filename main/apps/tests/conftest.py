# from pytest_factoryboy import register
# from main.apps.tests.factories import ManagerFactory


# register(ManagerFactory)


from pytest_factoryboy import register
from main.apps.tests.factories import (
    ManagerFactory,
    TransportFactory,
    HotelFactory,
    FlightFactory,
    OutfitFactory,
    GuideFactory,
)


register(ManagerFactory)
register(TransportFactory)
register(HotelFactory)
register(FlightFactory)
register(OutfitFactory)
register(GuideFactory)
