from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from ..common.models import BaseModel, BaseMeta
from .managers.user import UserManager
from ..package.models import TourPackage



class Region(BaseModel):
    title = models.CharField(max_length=200)

    class Meta(BaseMeta):
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    def __str__(self):
        return f'{self.title}'
    

class AgentIDTypeChoices(models.TextChoices):
    NMA1 = 'NMA1', _('NMA1')
    NMA2 = 'NMA2', _('NMA2')
    NMA3 = 'NMA3', _('NMA3')
    NMA4 = 'NMA4', _('NMA4')
    QQN = 'QQN', _('QQN')
    MRN = 'MRN', _('MRN')
    AZN = 'AZN', _('AZN')
    TAS = 'TAS', _('TAS')
    SKD = 'SKD', _('SKD')


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone_number = models.CharField(max_length=255, unique=True,
                             verbose_name=_("Телефонный номер"))
    full_name = models.CharField(
        null=True, blank=True, max_length=50, verbose_name=_("Имя Фамилия"))
    email = models.EmailField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regions', null=True)
    is_moderator = models.BooleanField(default=False)
    is_for_flight = models.BooleanField(default=False)
    is_for_hotel = models.BooleanField(default=False)
    is_for_visa = models.BooleanField(default=False)
    is_working_with_agent = models.BooleanField(default=False)
    is_for_finance = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_outfit = models.BooleanField(default=False)
    agent_id = models.CharField(max_length=255, choices=AgentIDTypeChoices.choices, null=True, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False, 
        help_text=_(
            "Designates whether the user can log into this admin site.",
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting account."
        ),
    )
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    percent = models.IntegerField(null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    class Meta(BaseMeta):
        ordering = ("-id",)
        verbose_name = _("user")
        verbose_name_plural = _("users")


    def __str__(self):
        return f"{self.full_name}"
    


class AgentCalculation(BaseModel):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tourpackage = models.ForeignKey(TourPackage, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)


    class Meta(BaseMeta):
        verbose_name = _("AgentCalculation")
        verbose_name_plural = _("AgentCalculation")


    def __str__(self):
        return f'{self.id}'