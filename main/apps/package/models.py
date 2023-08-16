import os
from django.db import models
from django.utils.translation import gettext as _
from ..common.models import BaseModel, BaseMeta
from ..transport.models import Transport
from ..hotel.models import Hotel
from ..outfit.models import Outfit
from ..flight.models.flight import Flight
from ..employee.models import Manager, Guide
from django.utils import timezone
from django.utils.text import slugify

def upload_landing_images(instance, filename):
    path = "landing_images/"
    filename_without_extension, extension = os.path.splitext(filename.lower())
    timestamp = timezone.now().strftime("%Y-%m-%d.%H-%M-%S")
    filename = f"{slugify(filename_without_extension)}.{timestamp}{extension}"
    return os.path.join(path, filename)


class StatusChoices(models.TextChoices):
    Created = 'Created', _('Created')
    Guide_expectations = 'Guide expectations', _('Guide expectations')
    In_adding_users = 'In adding users', _('In adding users')
    Pending_payment = 'Pending payment', _('Pending payment')
    Submitted_for_visa = 'Submitted for visa', _('Submitted for visa')
    Waiting_for_visa = 'Waiting for visa', _('Waiting for visa')
    Ready_to_send = 'Ready to send', _('Ready to send')
    Sent = 'Sent', _('Sent')
    Waiting_to_arrive_back = 'Waiting to arrive back', _('Waiting to arrive back')
    Closed = 'Closed', _('Closed')


class TourPackage(BaseModel):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    additional_expense = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    number_of_seats = models.PositiveIntegerField()
    price_for_person = models.DecimalField(max_digits=20, decimal_places=2)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    hotel = models.ManyToManyField(Hotel)
    outfit = models.ManyToManyField(Outfit)
    transport = models.ManyToManyField(Transport)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='tourpackage_managers', null=True)
    guide = models.ManyToManyField(Guide)
    date_data = models.JSONField(null=True, blank=True)
    outfit_data = models.JSONField(null=True, blank=True)
    hotel_data = models.JSONField(null=True, blank=True)
    status = models.CharField(
        max_length=100, 
        choices=StatusChoices.choices,
        default=StatusChoices.Created 
        )
    is_active = models.BooleanField(default=True)
    currency = models.DecimalField(max_digits=20, decimal_places=2, null=True)


    class Meta(BaseMeta):
        verbose_name = _("TourPackage")
        verbose_name_plural = _("TourPackages")


    def __str__(self):
        return f'{self.title}'
    


class TourPackageBook(BaseModel):
    tourpackage = models.ForeignKey(TourPackage, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    is_viewed = models.BooleanField(default=False)

    class Meta(BaseMeta):
        verbose_name = _("TourPackageBook")
        verbose_name_plural = _("TourPackageBooks")


    def __str__(self):
        return f'{self.full_name}'
    


class Contact(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    phone_number_1 = models.CharField(max_length=50, null=True, blank=True)
    phone_number_2 = models.CharField(max_length=50, null=True, blank=True)
    landing_img = models.ImageField(upload_to=upload_landing_images, null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    class Meta(BaseMeta):
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


    def __str__(self):
        return f'{self.title}'