import os
from django.db import models
from django.utils import timezone
from ..common.models import BaseMeta, BaseModel
from ..hotel.models import Hotel
from ..package.models import TourPackage
from ..visa.models import Visa
from django.utils.text import slugify
from django.utils.translation import gettext as _
from ..common.utils import upload_images


class Client(BaseModel):
    tour_package = models.ForeignKey(TourPackage, on_delete=models.SET_NULL, null=True, related_name='tourpackage_clients')
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, related_name='hotel_clients')
    visa  = models.ForeignKey(Visa, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=200)
    dob = models.DateField()
    passport_expiration_date = models.DateField()
    series = models.CharField(max_length=100)
    series_number = models.PositiveIntegerField()
    passport_img = models.ImageField(upload_to=upload_images(instance='self', path='client_images/'), null=True)
    room_type = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)
    visa_file = models.FileField(upload_to=upload_images(instance='self', path='visa_files/'), null=True)
    is_badge = models.BooleanField(default=False)
    outfit_size = models.CharField(max_length=50, null=True)
    

    class Meta(BaseMeta):
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")


    def __str__(self):
        return f'{self.full_name}'
    


class Partner(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    dob = models.DateField()
    passport_expiration_date = models.DateField()
    series = models.CharField(max_length=100)
    series_number = models.PositiveIntegerField()
    passport_image = models.ImageField(upload_to=upload_images(instance='self', path='pass_partner_images/'), null=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)
    visa_file = models.FileField(upload_to=upload_images(instance='self', path='pass_visa_files/'), null=True)
    is_badge = models.BooleanField(default=False)
    outfit_size = models.CharField(max_length=50, null=True)
    

    class Meta(BaseMeta):
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")


    def __str__(self):
        return f'{self.full_name}'


class VisaClient(BaseModel):
    visa  = models.ForeignKey(Visa, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=200)
    dob = models.DateField()
    passport_expiration_date = models.DateField()
    series = models.CharField(max_length=100)
    series_number = models.PositiveIntegerField()
    passport_img = models.ImageField(upload_to=upload_images(instance='self', path='visa_client_pass_imgs/'), null=True)
    room_type = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)
    visa_file = models.FileField(upload_to=upload_images(instance='self', path='visa_client_files/'), null=True)
    is_badge = models.BooleanField(default=False)
    

    class Meta(BaseMeta):
        verbose_name = _("VisaClient")
        verbose_name_plural = _("VisaClients")


    def __str__(self):
        return f'{self.full_name}'
    


class VisaPartner(BaseModel):
    visa_client = models.ForeignKey(VisaClient, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200)
    dob = models.DateField()
    passport_expiration_date = models.DateField()
    series = models.CharField(max_length=100)
    series_number = models.PositiveIntegerField()
    passport_image = models.ImageField(upload_to=upload_images(instance='self', path='visa_partner_pass_imgs/'), null=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    remained_amount = models.DecimalField(max_digits=20, decimal_places=2)
    

    class Meta(BaseMeta):
        verbose_name = _("Partner")
        verbose_name_plural = _("Partners")


    def __str__(self):
        return f'{self.full_name}'